#Kahn's Algo 

def kahn(graph, visited, indegree,topo_sort):
    queue = []
    for key in visited:
        if indegree[key] == 0:
            queue.append(key)
            visited[key]=True
    while queue:
        temp = queue.pop(0)
        topo_sort.append(temp)
        for child in graph[temp]:
            if not visited[child]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    visited[child] = True


#driver code
inp = [[1,2],[2,3],[1,3],[4,1],[6,1],[6,3],[4,3],[5,3],[8,1],[1,7],[9,7],[9,8]]
graph = {}
visited = {}
inDegree = {}
topo_sort = []
n = 9

for i in range(1, n+1):
    graph[i]=[]
    visited[i]=False
    inDegree[i] = 0

for u,v in inp:
    graph[u].append(v)
    inDegree[v] += 1

kahn(graph, visited, inDegree,topo_sort)
print(topo_sort)
