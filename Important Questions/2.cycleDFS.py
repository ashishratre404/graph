"""
    1-----------2                     1---------5
    |                                 |\        |
    |                                 |  \      |
    3----------4                      |   3     |
                                      |  /      |
                                      2 --------4
Unidired graph 1                    undirected graph 2
(no cycle)                           (cycle 1-2-3-1)

"""                       

def dfs_cycle(graph, visited, node, parent):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            return dfs_cycle(graph, visited, child, node)
        else:
            if child != parent:
                return True
    return False

#graph1
# inp = [[1,2], [1,3], [3,4]]
# n = 4

# graph 2
inp = [[1,2], [1,3], [1,5], [2,4], [2,3], [4,5]]
n=5

graph = {}
visited = {}
startNode = 1
parent = -1  #parent for starting node is -1
for i in range(1,n+1):
    graph[i] = []
    visited[i] = False

for u,v in inp:
    graph[u].append(v)
    graph[v].append(u)

a = dfs_cycle(graph, visited, startNode, parent)
print(a)
