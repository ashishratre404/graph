def bfs(graph, visited):
    startNode = 1
    queue = []
    queue.append(startNode)
    visited[startNode] = True
    while queue:
        node = queue.pop(0)
        print(node)
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True

        



inp = [[1,2], [1,5], [2,3], [2,4], [2,5], [3,4], [3,6], [4,5], [4,6], [5,6]]
n = 6
graph = {}
visited = {}
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False

for u, v in inp:
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, visited)
