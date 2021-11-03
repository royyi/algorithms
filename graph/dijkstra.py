# Roy Yi
# 9/21/21
# Implement dijkstra's shortest path algorithm

import heapq

def sssp_dijkstra(graph, s):
    '''finds the shortest distance from s to any other vertex in the graph
       edge weights in G must be nonnegative'''
       
    Q = [(0, s)] + [(float('inf'), v) for v in graph if v != s]
    d = {v: 0 if v == s else float('inf') for v in graph}
    finished = set() 
    
    while Q:
        dist, u = heapq.heappop(Q)

        if u in finished: continue
        finished.add(u)

        for v in graph[u]:
            if d[u] + graph[u][v] < d[v]:
                d[v] = d[u] + graph[u][v]
                heapq.heappush(Q, (d[v], v))

    return d

def main():
    graph = {
        'A': {'B': 50, 'C': 45, 'D': 10},
        'B': {'C': 10, 'D': 15},
        'C': {'E': 30},
        'D': {'A': 10, 'E': 15},
        'E': {'B': 20, 'C': 35, 'F': 3},
        'F': {},
    }

    print(sssp_dijkstra(graph, 'A'))

if __name__ == "__main__":
    main()

# while we are not done:
# expand the closest unvisited node from s and relax all adjacent edges

# represent priority queue objects as tuples: (priority, object)
