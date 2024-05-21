import argparse

def generate_hamilton():
    pass
def generate_non_hamilton():
    pass
def generate_graph(option, number_of_nodes, saturation=50):
    pass
def print_graph(grapg):
    pass
def euler(graph):
    pass
def hamilton(graph):
    pass
def export(graph):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--hamilton',action='store_true', help='Graph with Hamilton Cycle')
    group.add_argument('--non-hamilton',action='store_true', help='Graph without Hamilton Cycle')
    args = parser.parse_args()
    number_of_nodes = int(input("nodes> "))
    if args.hamilton:
        saturation = int(input("saturation> "))
        graph = generate_graph(generate_hamilton, number_of_nodes, saturation)
    elif args.non-hamilton:
        graph = generate_graph(generate_non_hamilton, number_of_nodes)
    while(True):
        choice=input("action> ").strip().lower()
        if choice == "help":
            print("""Help        Show this message
Print       Print the graph
Euler       Find Euler Cycle in the graph
Hamilton    Find Hamilton Cycele in the graph
Export      Export the graph to tickzpicture
Exit        Exits the program (same as ctrl+D)""")
        elif choice=="print":
            print_graph(graph)
        elif choice=="euler":
            euler(graph)
        elif choice=="hamilton":
            hamilton(graph)
        elif choice=="export":
            export(graph)
        elif choice=="exit":
            break
        else:
            print("To view possible actions type: Help")