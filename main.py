import argparse
from generate_graph import generate_non_hamilton, generate_graph
from functions import get_neighbours, export_to_latex, print_graph
from algorithms import hamilton, euler

def euler(graph):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--hamilton' ,action='store_true', help='Graph with Hamilton Cycle')
    group.add_argument('--non-hamilton' ,action='store_true', help='Graph without Hamilton Cycle')
    args = parser.parse_args()
    number_of_nodes = int(input("nodes> "))
    if args.hamilton:
        saturation = int(input("saturation> "))
        graph = generate_graph(number_of_nodes, saturation)
    elif args.non_hamilton:
        graph = generate_non_hamilton(number_of_nodes)
    while(True):
        choice=input("action> ").strip().lower()
        if choice == "help":
            print("""Help        Show this message
Print       Print the graph
Euler       Find Euler Cycle in the graph
Hamilton    Find Hamilton Cycle in the graph
Export      Export the graph to tickzpicture
Exit        Exits the program (same as ctrl+D)""")
        elif choice=="print":
            print_graph(graph)
        elif choice=="euler":
            print(euler(graph))
        elif choice=="hamilton":
            print(hamilton(number_of_nodes,graph))
        elif choice=="export":
            export_to_latex(graph,number_of_nodes)
        elif choice=="exit":
            break
        else:
            print("To view possible actions type: Help")
