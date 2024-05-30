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
