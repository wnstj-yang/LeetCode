class Solution(object):
    def criticalConnections(self, n, connections):
        # 1. 그래프 생성 (인접 리스트)
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        depth = [0] * n   # 현재 노드의 "위치 (높이)"
        reach = [0] * n   # "이 노드가 갈 수 있는 가장 위 depth"
        result = []

        def dfs(node, parent, d):
            # 2. 방문 처리
            visited[node] = True
            depth[node] = d
            reach[node] = d   # 처음엔 자기 자신까지

            # 3. 인접 노드 탐색
            for nxt in graph[node]:

                # ❗ 부모는 제외 (핵심)
                if nxt == parent:
                    continue

                # 4. 아직 방문 안 한 경우 (트리 edge)
                if not visited[nxt]:
                    dfs(nxt, node, d + 1)

                    # 🔥 자식이 위로 갈 수 있는 정보 반영
                    reach[node] = min(reach[node], reach[nxt])

                    # 🔥 핵심 조건 (critical 판단)
                    if reach[nxt] > depth[node]:
                        result.append([node, nxt])

                # 5. 이미 방문된 경우 (cycle 발견)
                else:
                    # 🔥 위로 올라가는 경로 발견
                    reach[node] = min(reach[node], depth[nxt])

        # 6. DFS 시작
        dfs(0, -1, 0)

        return result