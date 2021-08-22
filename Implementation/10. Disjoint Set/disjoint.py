class DisjSet():
    def __init__(self,n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def findParent(self, node):
        if node == self.parent[node]:
            return node
       # return self.findParent(self.parent[node])          this will return parent without compressing path
        self.parent[node] = self.findParent(self.parent[node])  # path is compressed now
        return self.parent[node]
    
    def Union(self, x, y):
        u = self.findParent(x)
        v = self.findParent(y)

        if u == v:  # if both are alraedy in same set
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[v] = u
            self.rank[u] += 1


# Driver code
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
if obj.findParent(4) == obj.findParent(0):
	print('Yes')
else:
	print('No')
if obj.findParent(1) == obj.findParent(0):
	print('Yes')
else:
	print('No')

