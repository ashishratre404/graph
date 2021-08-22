class Solution:
    def numIsland(self, grid):
        if not grid: return None
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collection.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft() # if we write pop() then it will be iterative version of dfs
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))


        for r in len(rows):
            for c in len(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

