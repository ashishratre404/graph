

def dfs(graph, startNode, visited):
    print(startNode)
    visited[startNode] = True
    for child in graph[startNode]:
        if not visited[child]:
            dfs(graph, child, visited)




inp = [[1,2], [1,5], [2,3], [2,4], [2,5], [3,4], [3,6], [4,5], [4,6], [5,6]]
n = 6
graph = {}
visited = {}
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False

for i, j in inp:
    graph[i].append(j)
    graph[j].append(i)


dfs(graph, 1, visited)