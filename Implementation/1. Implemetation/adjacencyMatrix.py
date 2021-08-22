# BUILD GRAPH FOR THIS INPUT 

# UN DIRECTED GRAPH
# 7 9
# A B
# A C
# A F
# C E
# C F
# C D
# D E
# D G
# G F

# DIRECTED WEIGHTED GRAPH
# 6 7
# A B 4
# A C 2
# B C 5
# B D 10
# C E 3
# D F 11
# E D 4



def graphMatrixI(matrix):
    r,c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()

v,e = map(int, input().split())
matrix = [[0]*v for i in range(v)]

'''
# For Un-directed
for i in range(e):
    u,v = map(str, input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    matrix[u][v] = 1 # un-directed : [u][v] = [v][u] = 1, if directed then only do [u][v] = 1
    matrix[v][u] = 1
'''

# Directed
for i in range(e):
    u,v,w = map(str, input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    w = int(w)
    matrix[u][v] = w  # w --> wight/cost of edge and only [u][v] means it is directed graph



graphMatrixI(matrix)