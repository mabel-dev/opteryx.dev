import re
import sys
from pathlib import Path

def hex_to_rgb(hex_color: str):
    """Convert hex color (#RRGGBB) to an (R, G, B) tuple."""
    hex_color = hex_color.strip("#")
    if len(hex_color) == 3:
        hex_color = "".join([c*2 for c in hex_color])  # Expand shorthand (#ABC → #AABBCC)
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rgb_to_luminance(rgb: tuple):
    """Convert (R, G, B) to relative luminance using the WCAG formula."""
    def adjust(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def contrast_ratio(fg: tuple, bg: tuple):
    """Calculate contrast ratio between foreground and background colors."""
    lum_fg = rgb_to_luminance(fg)
    lum_bg = rgb_to_luminance(bg)
    lighter, darker = max(lum_fg, lum_bg), min(lum_fg, lum_bg)
    return (lighter + 0.05) / (darker + 0.05)

def extract_rules(css_content: str):
    """
    Extract CSS selectors, colors, and background colors from the CSS file.
    Returns a list of (selector, foreground_color, background_color) tuples.
    """
    rules = []
    css_blocks = re.findall(r'([^{]+)\{([^}]+)\}', css_content)  # Extract selectors and properties

    for selector, properties in css_blocks:
        color_match = re.search(r'color:\s*(#[0-9a-fA-F]{3,6}|rgb\([\d\s,]+\));', properties)
        bg_color_match = re.search(r'background(?:-color)?:\s*(#[0-9a-fA-F]{3,6}|rgb\([\d\s,]+\));', properties)

        if color_match and bg_color_match:
            rules.append((selector.strip(), color_match.group(1), bg_color_match.group(1)))

    return rules

def validate_css_file(css_file: str):
    """Reads a CSS file, checks contrast ratios, and prints failures with selectors."""
    with open(css_file, "r", encoding="utf-8") as file:
        css_content = file.read()

    rules = extract_rules(css_content)

    failed_selectors = []
    for selector, fg_hex, bg_hex in rules:
        fg_rgb = hex_to_rgb(fg_hex)
        bg_rgb = hex_to_rgb(bg_hex)
        ratio = contrast_ratio(fg_rgb, bg_rgb)

        if ratio < 4.5 and fg_hex != bg_hex:
            failed_selectors.append((selector, fg_hex, bg_hex, ratio))

    return failed_selectors

def find_css_files(root_dir="."):
    """Find all CSS files in the given directory and subdirectories."""
    return list(Path(root_dir).rglob("*.css"))

def test_css_files():
    css_files = find_css_files()

    if not css_files:
        print("No CSS files found.")
        sys.exit(1)

    failures = []
    for css_file in css_files:
        failed_selectors = validate_css_file(css_file)
        if failed_selectors:
            failures.append((css_file, failed_selectors))

    if failures:
        print("\n🚨 **Contrast Check Failed!** 🚨\n")
        for css_file, failed_selectors in failures:
            print(f"File: {css_file}")
            for selector, fg, bg, ratio in failed_selectors:
                print(f"  ❌ {selector} - Foreground: {fg}, Background: {bg}, Contrast: {ratio:.2f}")
            print("-" * 50)
        assert False, "Some CSS files failed the contrast check!"
    else:
        print("✅ All CSS files passed the contrast check!")

if __name__ == "__main__":
    test_css_files()
