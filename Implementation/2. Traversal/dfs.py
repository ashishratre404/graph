
def dfs(graph, node, visited):
    visited[node] = True
    dfs_traversal_rsult.append(node)
    for child in graph[node]:
        if not visited[child]:
            dfs(graph, child, visited) 


#Driver code

#disconnected graph: node 1,2,3,4,5,6,7 is one component and node 8,9 is other.
inp = [[1,2],[1,3],[2,4],[3,4],[3,5],[5,6],[5,7],[6,7],[8,9]] #edges
n = 9 #node
graph = {}
visited = {}
dfs_traversal_rsult = []
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False

for u,v in inp:
    graph[u].append(v)
    graph[v].append(u)

for node in graph:                # this is necessary in case of disconnected graph
    if not visited[node]:
        dfs(graph, node, visited)

print(dfs_traversal_rsult)