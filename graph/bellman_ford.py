# Roy Yi
# 10/20/21
# Implement bellman-ford algorithm

def sssp_bellman(vertices, edges, s):
    '''find shortest path in a graph that may have negative edges'''
    d = {v: 0 if v == s else float('inf') for v in vertices}

    # relax each edge of G for V-1 passes
    for i in range(len(vertices) - 1):
        for u, v, w in edges: 
            d[v] = min(d[v], d[u] + w)

    # if any distance updates on pass V, there must be a negative cycle
    for u, v, w in edges: 
        if d[u] + w < d[v]:
            return "Graph contains negative cycle"

    return d


def main():
    # list of edges representation of graph
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [('A', 'B', -1), ('A', 'C', 4), ('B', 'C', 3), ('B', 'D', 2), 
             ('B', 'E', 2), ('D', 'B', 1), ('D', 'C', 5), ('E', 'D', -3)]

    print(sssp_bellman(vertices, edges, 'A'))

if __name__ == "__main__":
    main()
