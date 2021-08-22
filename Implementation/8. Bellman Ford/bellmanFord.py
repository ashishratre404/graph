inp = [[1,2,2],[1,3,1],[2,3,-2],[2,4,2],[3,5,-1],[4,5,1]]
n = 5
dist = {}
inf = 10**8+1
for i in range(1, n+1):
    dist[i] = inf

dist[1] = 0   #distance of source node is zero

for _ in range(n-1):
    for u,v,w in inp:  # parent_node, child_node, cost of edge
        if dist[u] < inf and dist[u] + w < dist[v]:
            dist[v] = w + dist[u]
print(dist)