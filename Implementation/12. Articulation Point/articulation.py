def dfs(graph,node, visited, par, intime, lowtime):
    global timer 
    global root

    visited[node] = True
    intime[node] = timer 
    lowtime[node] = timer 
    timer += 1

    c = 0
    for child in graph[node]:
        if not visited[child]:
            if root == node:
                c += 1
            dfs(graph, child, visited, node, intime, lowtime)
            if intime[node] <= lowtime[child] and node != root:
                print("Articulation Point: -->", format(node))
            lowtime[node] = min(lowtime[node], lowtime[child])
        else:
            if child != par:
                lowtime[node] = min(lowtime[node],intime[child])
        
    if c> 1:
        print("Articulation Point:-->", node)


#driver code
inp = [[1,2],[2,3],[3,1],[2,4],[2,5],[4,5]]
n = 5

graph={}
visited={}
intime={}
lowtime={}
timer = 1
for i in range(1, n+1):
    graph[i] = []
    visited[i] = False
    intime[i] = None
    lowtime[i] = None

root = 1

for u,v in inp:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited, -1, intime, lowtime)
