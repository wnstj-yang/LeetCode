from collections import deque

class Solution(object):
    def numIslands(self, grid):
        def check_range(x, y):
            if x < 0 or x >= N or y < 0 or y >= M:
                return False
            return True

        def bfs(s, e):
            queue = deque()
            queue.append((s, e))
            visited[s][e] = True
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]            
                    ny = y + dy[d]
                    
                    if check_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        N, M = len(grid), len(grid[0])
        visited = [[False] * M for _ in range(N)]
        count = 0

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count
        