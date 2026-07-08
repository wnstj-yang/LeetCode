from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return 0

        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        N = len(grid)

        distances = [[-1] * N for _ in range(N)]
        queue = deque()

        for i in range(N):
            for j in range(N):
                 if grid[i][j] == 1:
                    distances[i][j] = 0
                    queue.append((i, j))
        
        # 1. 큐를 활용하여 도둑이 있는 곳부터 시작해서 각 칸의 안전도 즉, 거리를 구한다.
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or distances[nx][ny] != -1:
                    continue
                queue.append((nx, ny))
                distances[nx][ny] = distances[x][y] + 1

        # 2. 경로를 탐색할 때 우선순위 큐를 활용하여 안전도가 높은 경로를 찾아나선다
        best = [[-1] * N for _ in range(N)] # 현재까지의 경로에서 안전도 값을 표현한다.
        best[0][0] = distances[0][0]
        pq = [(-distances[0][0], 0, 0)] # 안전도가 높은 값 + 좌표

        while pq:
            until_now, x, y = heapq.heappop(pq)
            plus_until_now = -until_now

            # 현재 경로의 안전도 값 < 현재까지의 경로의 안전도 값

            if x == N - 1 and y == N - 1:
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                new_dist = min(distances[nx][ny], plus_until_now)
                # 경로 탐색 시 현재까지의 경로 값보다 안전도가 높으면 진행
                if new_dist > best[nx][ny]:
                    best[nx][ny] = new_dist
                    heapq.heappush(pq, (-new_dist, nx, ny))

        return best[N - 1][N - 1]





