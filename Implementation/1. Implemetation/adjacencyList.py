
# Given Graph : 

# {
#     'A': ['B','C'],
#     'B': ['A','D'],
#     'C': ['A','D','E'],
#     'D': ['B','C','E'],
#     'E': ['C','D']
# }


all_edges = [ ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

class Graph:
    def __init__(self, Nodes, isDirected) -> None:
        self.nodes = Nodes
        self. adj_list = { }
        self.isDirected = isDirected

        for nodes in self.nodes:
            self.adj_list[nodes] = []
    
    def add_edges(self, u, v):
        self.adj_list[u].append(v)
        if not self.isDirected:
            self.adj_list[v].append(u)

    def degree(self, node):
        if not self.isDirected:
            return len(self.adj_list[node])
        else:
            return 'Directed graph: need to implement indegree and outdegree'

    def print_adjList(self):
        for node in self.adj_list:
            print(node, "-->", self.adj_list[node])
    


nodes = ['A', 'B', 'C', 'D', 'E']
gp = Graph(nodes, isDirected=False)

for u,v in all_edges:
    gp.add_edges(u,v)

gp.print_adjList()
print(gp.degree('B'))
