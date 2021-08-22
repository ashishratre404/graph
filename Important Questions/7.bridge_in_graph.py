
def dfs(graph, startNode, visited, intime, lowtime, parent):
    global timer
    visited[startNode] = True
    intime[startNode] = timer
    lowtime[startNode] = timer
    timer += 1
    for child in graph[startNode]:
        if not visited[child]:
            dfs(graph, child, visited, intime, lowtime, startNode)
            if intime[startNode] < lowtime[child]:
                print('Bridge found at: ', startNode, '-', child)
            lowtime[startNode] = min(lowtime[child], lowtime[startNode])
        else:
            if child != parent:
                lowtime[startNode] = min(intime[child], lowtime[startNode])



inp = [[1,2], [1,3], [2,4], [3,4], [3,5], [5,6], [5,7], [6,7]]
n = 7
graph = {}
visited = {}
intime = {}
lowtime = {}
timer = 1

for i in range(1, n+1):
    graph[i] = []
    visited[i] = False
    intime[i] = None
    lowtime[i] = None

for u, v in inp:
    graph[u].append(v)
    graph[v].append(u)


dfs(graph, 1, visited, intime, lowtime, -1) # startNode = 1, parent = -1