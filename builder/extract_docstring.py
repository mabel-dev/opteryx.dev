import re
import ast

known_headers = (
    "parameters",
    "arguments",
    "args",
    "returns",
    "yields",
    "example",
    "examples",
    "note",
    "warning",
    "raises",
)


def strip_non_alpha_num(raw):
    pattern = re.compile(r"[\W_]+")
    return pattern.sub("", raw)


def create_md_content(node, title=None, cls=False):

    current_header = ""

    doc_string = ast.get_docstring(node) or ""

    cache = ""
    if not cls:
        cache = "<dl><dt>"
        cache += f"<b>{title}</b>"
        if isinstance(node, ast.FunctionDef):
            cache += " ("
            cache += ", ".join([a.arg for a in node.args.args if a.arg != "self"])
            cache += ")"
        cache += "</dt><dd>"

    last_indent = -1
    for line in doc_string.splitlines():
        indent = measure_indent(line)
        line = line.strip()

        if len(line) == 0:
            cache += "\n"

        header = [h for h in known_headers if strip_non_alpha_num(line.lower()) == h]
        if len(header) == 1:
            if current_header in ["Example", "Examples"]:
                cache += "\n~~~\n"
            current_header = header.pop().title()
            cache += f"\n<p><b>{current_header}</b></p><ul>"
            last_indent = 100
            continue

        if last_indent == indent:
            # if its the same indent, its a line continuation
            if current_header in ["Example", "Examples"]:
                cache += "\n" + line
            else:
                cache += " " + line
        else:
            if last_indent > indent:
                # this is an inner_header
                parts = line.split(":")
                for index, part in enumerate(parts):
                    if index == 0 and len(part.split()) > 0:
                        print("********", current_header)
                        if current_header not in ["Example", "Examples"]:
                            cache += "<li>" + part + ": "
                        else:
                            cache += "<br /> \n<code>\n" + part + "  "
                    elif len(part.split()) == 0:
                        pass
                    else:
                        cache += part
            else:
                # this is the body of the inner_header
                cache += "\n</br>" + line + "</li>"

        last_indent = indent

    if current_header in ["Example", "Examples"]:
        cache += "\n</code>\n"
    else:
        cache += "</ul>"

    # print(cache)
    if not cls:
        cache += "</dd></dl>\n"
    return cache
