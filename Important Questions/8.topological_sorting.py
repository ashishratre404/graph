# Only applicable for DAG (Directed Acyclic Graph)
def topo_sort(graph, visited, indegree):
    q = []
    for key in visited:
        if indegree[key] == 0:
            q.append(key)
            visited[key] = True
    
    while q:
        node = q.pop(0)
        topo_result.append(node)
        for child in graph[node]:
            if not visited[child]:
                indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
                visited[child] = True

inp = [[1,2],[2,3],[1,3],[4,1],[6,1],[6,3],[4,3],[5,3],[8,1],[1,7],[9,7],[9,8]]
n = 9

graph = {}
visited = {}
topo_result = []
indegree = {}

for i in range(1, n+1):
    graph[i] = []
    visited[i] = False
    indegree[i] = 0

for u, v in inp:
    graph[u].append(v)
    indegree[v] += 1 


topo_sort(graph, visited, indegree)
print(topo_result)