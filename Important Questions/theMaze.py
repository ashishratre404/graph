
class Solution:
    def hasPath(self, maze, start, destination):
        m, n, visited = len(maze), len(maze[0]), set()
        def dfs(x, y):
            if (x, y) not in visited:
                visited.add((x, y))
            else:
                return False
            if [x, y] == destination:
                return True
            
            for i, j in (0, -1), (0, 1), (-1, 0), (1, 0):
                new_x, new_y = x, y
                while 0 <= new_x + i < m and 0 <= new_y + j < n and maze[new_x+i][new_y+j] != 1:
                    new_x += i
                    new_x += j
                if dfs(new_x, new_y):
                    return True
            return False
        return(dfs(*start))