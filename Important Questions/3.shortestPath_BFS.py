def bfs(graph, visited, distance):
    startNode = 1
    queue = []
    queue.append(startNode)
    visited[startNode] = True
    distance[startNode] = 0
    while queue:
        node = queue.pop(0)
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True
                distance[child] = distance[node] + 1

        



inp = [[1,2], [1,5], [2,3], [2,4], [2,5], [3,4], [3,6], [4,5], [4,6], [5,6]]
n = 6
graph = {}
visited = {}
distance = {}
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False
    distance[i] = None

for u, v in inp:
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, visited, distance)
print(distance)