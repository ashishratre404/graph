# 684. Redundant Connection

# Given:
#   -> A graph with n nodes and n edges

#     Goal:
#     -> return edge whose removal convert a Graph into a Tree

# Approach:
#     Tree: 1. every node are connected, 2. no cycle

#     Observation:
#     -> if graph has n nodes and n edges means it has cycle
#     Steps:
#         1. make all nodes as individual component and mark parent of itself
#         2. calulate size of component, say Rank
#             -> component of lower rank will be child of component with higher rank
#         3. connection is successful if root parent of both component is not same, if same means connection of this edge will form a cycle
        


class Solution:
    def findRedundantConnection(self, edges):
        par = [i for i in range(len(edges)+1)]  # marked every node as parent of itself
        rank = [1]*len(edges)+1      #here, rank means size of component
    
        def find(n):           #function to return root parent for any node
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):           # function for merging two components
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]