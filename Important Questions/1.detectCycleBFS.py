"""
    1-----------2                     1---------5                  1<--------2
    |                                 |\        |                  |        ^
    |                                 |  \      |                  |        |             
    3----------4                      |   3     |                  |        |               
                                      |  /      |                  V        |
                                      2 --------4                  3------->4
Unidired: graph 1                    undirected: graph 2          directed: graph3 
(no cycle)                           (cycle 1-2-3-1)            (cycle 1-3-4-2-1)

""" 

def isCycleBFS(graph, visited, parent):
    q = []
    startNode = 1
    q.append(startNode)
    visited[startNode] = True
    parent[startNode] = -1
    while q:
        node = q.pop(0)
        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                parent[child] = node
                print(parent)
            else:
                if parent[node] != child:
                    return True
    return False


#graph1
# inp = [[1,2], [1,3], [3,4]]
# n = 4

# graph 2 (un-directed)
inp = [[1,2], [1,3], [1,5], [2,4], [2,3], [4,5]]
n=5

#graph3 (directed)
# inp = [[1,3], [3,4], [4,2], [1,2]]
# n=4

graph = {}
visited = {}
parent = {}
for i in range(1,n+1):
    graph[i] = []
    visited[i] = False

for u,v in inp:
    graph[u].append(v)
    graph[v].append(u)

a = isCycleBFS(graph, visited, parent)
print(a)
