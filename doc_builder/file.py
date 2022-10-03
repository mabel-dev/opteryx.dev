import ast
import glob
from format_docstring import create_md_content


def get_file():
    ob = next(glob.iglob("../**/opteryx/connection.py", recursive=True))
    return ob

def class_header(title, node):
    cache = f"<dl><dt><h2>class <b>{title}</b>"
    cache += " ("
    cache += ", ".join([a.arg for a in node.args.args if a.arg != "self"])
    cache += ")"
    cache += "</h2>"
    return cache


def process_file(filepath):

    file_contents = ""
    with open(filepath, encoding="utf8") as fd:
        file_contents = fd.read()

    module = ast.parse(file_contents)

    cache = ""

    for node in ast.iter_child_nodes(module):

        if isinstance(node, ast.ClassDef):
            # cache += create_md_content(node, title=node.name)
            class_name = node.name
            child_nodes = list(ast.iter_child_nodes(node))

            child_nodes = [c for c in child_nodes if hasattr(c, "name")]

            init = [
                child_node
                for child_node in child_nodes
                if child_node.name == "__init__"
            ]
            if len(init) > 0:
                init = init.pop()
                cache += class_header(node.name, init) + create_md_content(init, node.name, True) + "</dd></dl>"

            for child_node in [
                child_node
                for child_node in child_nodes
                if not child_node.name.startswith("_")
            ]:
                print("method:", child_node.name)
                if isinstance(child_node, ast.FunctionDef):
                    cache += create_md_content(child_node, title=child_node.name)

        if isinstance(node, ast.FunctionDef):
            if not node.name.startswith("_"):
                print("method:", node.name)
                cache += create_md_content(node, title=node.name)

    return cache


module = get_file()


print("module:", module)
save = module
doc = process_file(module)
save = "docs/get-started/python-client.md"

template_content = open(save, mode="r").read().split("<!--- start --->")[0]

doc = template_content + "<!--- start --->\n" + doc + "\n<hr><p>This file has been automatically generated from the source code.</p>"
open(save, "w").write(doc)
