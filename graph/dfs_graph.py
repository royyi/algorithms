# Roy Yi
# 9/21/21
# dfs on a DAG to find topological sort on its vertices

from collections import defaultdict

def dfs(graph, status, result, u):
    '''dfs starting from vertex u'''
    # if node is already visited, we reached same node from current dfs call
    if status[u] == 'visited':
        return False

    # if node is finished processing, we return
    elif status[u] == 'finished':
        return True

    status[u] = 'visited'

    # return false if any subcall detects a cycle
    for v in graph[u]:
        if dfs(graph, status, result, v) == False:
            return False

    # add finished  nodes to call stack
    status[u] = 'finished'
    result.append(u)

    return True

def topological_sort(graph):
    '''returns a topological ordering of the vertices of the graph'''
    status = {v: 'unvisited' for v in graph}
    result = []

    # main dfs routine: call dfs on each unvisited node
    for v in graph:
        if status[v] == 'unvisited':
            if dfs(graph, status, result, v) == False:
                return []

    # reverse of dfs call stack is topological ordering of vertices
    return result[::-1]


def main():
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 3), (2, 6), (3, 4), 
             (3, 5), (4, 7), (5, 7), (6, 7)]
    # edges = [(1, 0), (0, 2), (3, 1), (3, 2)]
    
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v]

    print(topological_sort(graph))

if __name__ == "__main__":
    main()
