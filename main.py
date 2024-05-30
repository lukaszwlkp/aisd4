import argparse
import random

def generate_non_hamilton(number_of_nodes):
    graph = generate_graph (number_of_nodes)
    random_node = random.choice(list(graph.keys()))
    graph[random_node] = []
    for i in range(1, number_of_nodes + 1):
        graph[i] = [x for x in graph[i] if x != random_node]

    return graph

def generate_graph(number_of_nodes, saturation = 50):
    vertices = list(range(1,number_of_nodes+1))
    random.shuffle(vertices)
    edges = [(vertices[i], vertices[(i + 1) % number_of_nodes]) for i in range(number_of_nodes)]
    edges = set(edges)

    number_of_edges = (number_of_nodes * (number_of_nodes - 1) //2)*(saturation/100)
    gap = 2
    i = - gap
    while len(edges) < number_of_edges:
        if i + 3 * gap < number_of_nodes :
            u, v, w = vertices[i + 1 * gap],vertices[i + 2 * gap], vertices[i + 3 * gap]
            if (u, v) not in edges and (v, w) not in edges and (u, w) not in edges:
                edges.add((u, v))
                edges.add((v, w))
                edges.add((u, w))
            i += 1
            if i + 3 * gap >= number_of_nodes:
                gap += 1
                i = -gap
        else:
            break
        
    graph = {i: [] for i in range(1,number_of_nodes+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def print_graph(graph):
    for v, neighbours in graph.items():
        print(f"{v} -> {' -> '.join(map(str, neighbours))}" if neighbours else f"{v} ->")
        
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
        graph = generate_graph(number_of_nodes, saturation)
    elif args.non-hamilton:
        graph = generate_non_hamilton(number_of_nodes)
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
