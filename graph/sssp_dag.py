# Roy Yi
# 10/18/21
# Shortest path in a DAG

from dfs_graph import topological_sort

def sssp_dag(graph, s):
    '''find shortest path from s to all other nodes'''
    d = {v: 0 if v == s else float('inf') for v in graph}

    order = topological_sort(graph)
    
    if not order:
        return "graph is not a DAG"

    for u in order:
        for v in graph[u]:
            # relax edge: graph[u][v] is the weight of edge u-v
            d[v] = min(d[v], d[u] + graph[u][v])

    return d 

def main():
    graph = {
        'A': {'B': 3, 'C': 6},
        'B': {'C': 4, 'D': 4, 'E': 11},
        'C': {'D': 8, 'G': 11},
        'D': {'E': -4, 'F': 5, 'G': 2},
        'E': {'H': 9},
        'F': {'H': 1},
        'G': {'H': 2},
        'H': {'A': 4}
    }

    print(sssp_dag(graph, 'A'))

if __name__ == "__main__":
    main()

# for each vertex taken in topological order, 
# relax all edges to the adjacent vertices
