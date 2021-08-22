parent = []
rank = []

def makeSet():
    for i in range(1,n+1):
        parent[i] = i
        rank[i] = 0

def findParent(node):
    if node == parent[node]:
        return node
    # return findParent(parent[node])  # this will return parent for any node without path compression
    return parent[node] = findParent(parent[node])    # path is compressed now

def union(u,v):
    u = findParent(u)
    v = findParent(v)

    if (rank[u] < rank[v]):
        parent[u] = v
    elif (rank[u] > rank[v]):
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1

