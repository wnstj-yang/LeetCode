class Solution(object):
    def spiralOrder(self, matrix):
        N, M = len(matrix), len(matrix[0])
        answer = []
        # 우하좌상
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0 # 방향
        time = 0 # 횟수
        x, y = 0, 0 # 좌표
        visited = [[False] * M for _ in range(N)] # 방문표시
        while time < N * M:
            visited[x][y] = True
            answer.append(matrix[x][y])
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위를 벗어나거나 같은 방향에서 방문한 경우라면 방향 변경
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
            # 좌표 초기화
            x, y = nx, ny
            time += 1
        return answer