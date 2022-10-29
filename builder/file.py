import ast
import glob
from format_docstring import create_md_content
from graph_lib import Graph

def get_file():
    ob = next(glob.iglob("../**/opteryx/connection.py", recursive=True))
    return ob

def function_node(node):
    args = []
    defaults = [c.value for c in node.args.defaults]
    defaults = ['🙂'] * (len(node.args.args) - len(defaults)) + defaults
    for index, arg in enumerate(node.args.args):
        if arg.arg != "self":
            if arg.annotation:
                args.append((arg.arg, arg.annotation.id, defaults[index]))
            else:
                args.append((arg.arg, None, defaults[index]))

    docstring = ast.get_docstring(node)

    kind = "function"
    # does the function have the property decorator?
    if any([d.id =="property" for d in node.decorator_list]):
        kind = "property"
    
    return_type = None
    # does the function have a return type hint?
    if node.returns:
        if isinstance(node.returns, ast.Subscript):
            return_type = f"{node.returns.value.id} [{node.returns.slice.id}]"
        else:
            return_type = node.returns.id

    return {
        "kind": kind,
        "name": node.name,
        "returns": return_type,
        "arguments": args,
        "description": docstring
    }

def process_file(filepath):

    graph = Graph()

    file_contents = ""
    with open(filepath, encoding="utf8") as fd:
        file_contents = fd.read()

    module = ast.parse(file_contents)
    module_docstring = ast.get_docstring(module)

    graph.add_node("root", kind="module", docstring=module_docstring)

    for node in ast.iter_child_nodes(module):

        if isinstance(node, ast.ClassDef):

            graph.add_node(node.name, kind="class")
            graph.add_edge("root", node.name, "contains")

            child_nodes = list(ast.iter_child_nodes(node))

            for child in [child for child in child_nodes if hasattr(child, "name")]:
                if child.name.startswith("_") and not child.name.startswith("__"):
                    continue
                if isinstance(child, ast.FunctionDef):
                    nid = str(id(child))
                    graph.add_node(nid, **function_node(child))
                    graph.add_edge("root", nid, "contains")
                else:
                    print(child.__dict__)

        elif isinstance(node, ast.FunctionDef):
            if not node.name.startswith("_"):
                graph.add_node(node.name, kind="method")
                graph.add_edge("root", node.name, "contains")


    print(graph.nodes(data=True))

    return graph


module = get_file()


print("module:", module)
save = module
doc = process_file(module)
save = "docs/get-started/python-client.md"

template_content = open(save, mode="r").read().split("<!--- start --->")[0]

doc = template_content + "<!--- start --->\n" + doc + "\n<hr><p>This file has been automatically generated from the source code.</p>"
#open(save, "w").write(doc)
