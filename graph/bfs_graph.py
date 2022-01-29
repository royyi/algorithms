# Roy Yi
# 9/21/21
# bfs on a graph and get shortest distance to each node (with unit edge weights)

from collections import defaultdict
from collections import deque

# returns the shortest path from s to any reachable vertex in the graph
def bfs(graph, s):
    Q = deque([s])
    d = {s: 0}

    while Q:
        u = Q.popleft()

        for v in graph[u]:
            if v not in d:
                d[v] = 1 + d[u]
                Q.append(v)

    return d

def main():
    graph = defaultdict(list)

    # undirected graph
    for u, v in [(0, 1), (0, 2), (2, 3), (2, 4), (3, 5), (3, 7), (3, 6), (4, 6), (7, 8), (4, 8)]:
        graph[u].append(v)
        graph[v].append(u)

    print(bfs(graph, 0))

if __name__ == "__main__":
    main()
