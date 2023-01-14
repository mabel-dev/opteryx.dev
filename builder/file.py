import ast
import glob

from graph_lib import Graph

CHILDS = ["property", "function"]


def get_file():
    ob = next(glob.iglob("../**/opteryx/connection.py", recursive=True))
    return ob


def function_node(node):
    args = []
    arg_defaults = [c.value for c in node.args.defaults]
    arg_defaults = ["🙂"] * (len(node.args.args) - len(arg_defaults)) + arg_defaults
    for index, arg in enumerate(node.args.args):
        if arg.arg != "self":
            if arg.annotation:
                args.append((arg.arg, arg.annotation.id, arg_defaults[index]))
            else:
                args.append((arg.arg, None, arg_defaults[index]))
    for index, arg in enumerate(node.args.kwonlyargs):
        args.append((arg.arg, None, None))

    docstring = ast.get_docstring(node)

    kind = "function"
    # does the function have the property decorator?
    if any([d.id == "property" for d in node.decorator_list]):
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
        "description": docstring,
    }


def process_file(filepath):

    graph = Graph()

    file_contents = ""
    with open(filepath, encoding="utf8") as fd:
        file_contents = fd.read()

    module = ast.parse(file_contents)
    module_docstring = ast.get_docstring(module)

    graph.add_node("root", kind="module", docstring=module_docstring)

    parent = "root"

    for node in ast.iter_child_nodes(module):

        if isinstance(node, ast.ClassDef):

            graph.add_node(node.name, kind="class", name=node.name)
            graph.add_edge("root", node.name, "contains")

            parent = node.name

            for child in ast.iter_child_nodes(node):
                if not hasattr(child, "name"):
                    print(child)
                    continue
                if child.name.startswith("_") and child.name != "__init__":
                    continue
                if isinstance(child, ast.FunctionDef):
                    nid = str(id(child))
                    graph.add_node(nid, **function_node(child))
                    graph.add_edge(parent, nid, "contains")
                else:
                    print(child.__dict__)

        elif isinstance(node, ast.FunctionDef):
            if not node.name.startswith("_"):
                graph.add_node(node.name, kind="method")
                graph.add_edge("root", node.name, "contains")

    return graph


def create_doc(graph):
    def _inner(nid):
        shard = ""
        # source, target, relation
        for s, t, r in graph.outgoing_edges(nid):
            node = graph[t]
            if node.get("kind") == "class":

                # class args are in a child
                init = [
                    i
                    for i in [graph[b] for a, b, c in graph.outgoing_edges(t)]
                    if i.get("name") == "__init__"
                ]
                desc = ""
                if init:
                    init = init.pop()
                    args = init.get("arguments")
                    desc = init.get("description")

                # name, type, default
                shard += f"<dl><dt><h2>class <b>{node['name']}</b> ({', '.join([n for n,t,d in args])})</h2></dt><dd>"
                if desc:
                    shard += desc
                shard += _inner(t)
                shard += "</dd></dl>"

            else:
                print(node.get("kind"))

        return shard

    return _inner("root")


module = get_file()


print("module:", module)
save = module
doc_graph = process_file(module)
doc = create_doc(doc_graph)
save = "docs/get-started/python-client.md"

print(doc)

template_content = open(save, mode="r").read().split("<!--- start --->")[0]

doc = (
    template_content
    + "<!--- start --->\n"
    + str(doc)
    + "\n<hr><p>This file has been automatically generated from the source code.</p>"
)
# open(save, "w").write(doc)
