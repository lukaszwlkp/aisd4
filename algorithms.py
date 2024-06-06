from functions import get_neighbours
from copy import deepcopy

def hamilton(n,graph):
    visited_list = [False] * (n + 1)
    Path = [0] * (n + 1)
    visited_count, k = 0, 2
    Path[1] = start = 1
    def hamiltonian(v):
        nonlocal visited_count, k
        visited_list[v] = True
        visited_count += 1
        neighbours = get_neighbours(graph,v)
        for i in neighbours:
            if i == start and visited_count == n:
                return True
            if not visited_list[i]:
                if (hamiltonian(i)):
                    Path[k] = v
                    k += 1
                    return True
        visited_list[v] = False
        visited_count -= 1
        return False
    hcycle_bool = hamiltonian(start)
    hcycle_path = Path[-1:0:-1] if hcycle_bool else None
    return hcycle_bool, hcycle_path

def dfs_euler(graph, v, stack):
    neighbours = get_neighbours(graph, v)
    for u in neighbours:
        graph[v].remove(u)
        graph[u].remove(v)
        dfs_euler(graph, u, stack)
    stack.append(v)
    
def euler(graph):
    graph_copy = deepcopy(graph)
    stack =[]
    dfs_euler(graph_copy, 1, stack)
    ecycle_bool = True if len(stack) > 1 else False
    ecycle_path = stack[::-1] if ecycle_bool else None
    return ecycle_bool, ecycle_path