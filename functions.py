def get_neighbours(graph, node):
    return graph.get(node, [])

def export_to_latex(graph, number_of_nodes):
    def export(graph):
        tikz_code = ""
        for node in range(1, number_of_nodes+1):
            tikz_code += f"    \\node[shape=circle,draw=black] ({chr(64+node)}) at ({node * 360/number_of_nodes}:3cm) {{{node}}};\n"
        for node in range(1, number_of_nodes+1):
            neighbours = get_neighbours(graph, node)
            for edge in neighbours:
                tikz_code += f"    \\path [-]({chr(64+node)}) edge ({chr(64+edge)});\n"
        return tikz_code

    tikz_code = f"\\begin{{tikzpicture}}\n{export(graph)}\\end{{tikzpicture}}"
    with open("graph.tex", "w") as f:
        f.write(tikz_code)
    print("Graph successfully exported")

def print_graph(graph):
    for v, neighbours in graph.items():
        print(f"{v} -> {' -> '.join(map(str, neighbours))}" if neighbours else f"{v} ->")