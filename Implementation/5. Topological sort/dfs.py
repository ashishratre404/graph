def dfs(graph, node, visited):
    visited[node] = True
    
    for child in graph[node]:
        if not visited[child]:
            dfs(graph, child, visited)
    dfs_traversal_rsult.append(node)



#Driver code

inp = inp = [[1,2],[2,3],[1,3],[4,1],[6,1],[6,3],[4,3],[5,3],[8,1],[1,7],[9,7],[9,8]]
n = 9 
graph = {}
visited = {}
dfs_traversal_rsult = []
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False

for u,v in inp:
    graph[u].append(v)
    graph[v].append(u)

#for node in graph:                # this is necessary in case of disconnected graph
#    if not visited[node]:
dfs(graph, 4, visited)

print(dfs_traversal_rsult)