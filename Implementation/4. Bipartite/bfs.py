class Solution:
    def isBipartite(self, graph: List[List[int]]):

        N = len(graph)
        col = [-1]*N

        for i in range(N):
            if col[i] != -1:
                continue
            q = deque()
            q.append((i,0))

            while q:
                node, color = q.popleft()
                if col[node] == -1:
                    col[node] = color
                    
                    for nx in graph[node]:
                        q.append((nx, color^1))
                if col[node] != color:
                    return False

        return True