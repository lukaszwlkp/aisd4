from functions import get_neighbours

def hamilton(n,graph):
    O = [False] * (n + 1)
    Path = [0] * (n + 1)
    visited, k = 0, 2
    Path[1] = start = 1
    def hamiltonian(v):
        nonlocal visited, k
        O[v] = True
        visited += 1
        neighbours = get_neighbours(graph,v)
        for i in neighbours:
            if i == start and visited == n:
                return True
            if not O[i]:
                if (hamiltonian(i)):
                    Path[k] = v
                    k += 1
                    return True
        O[v] = False
        visited -= 1
        return False
    hcycle_bool = hamiltonian(start)
    hcycle_path = Path[1:] if hcycle_bool else None
    return hcycle_bool, hcycle_path
