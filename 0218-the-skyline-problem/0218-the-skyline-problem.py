import heapq

class Solution:
    def getSkyline(self, buildings):
        # 1. 이벤트 생성
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))  # 시작점 (높이는 음수 → max heap처럼 사용)
            events.append((r, 0, 0))   # 끝점
        
        # 2. 정렬
        events.sort()

        # 3. heap 초기화 (높이, 끝나는 지점)
        heap = [(0, float('inf'))]  # 바닥
        result = []
        prev_height = 0

        # 4. sweep line
        for x, neg_h, r in events:
            
            # 🔽 이미 끝난 건물 제거
            while heap[0][1] <= x:
                heapq.heappop(heap)

            # 🔼 시작점이면 heap에 추가
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))

            # 📌 현재 최대 높이
            current_height = -heap[0][0]

            # 🔥 skyline 변화 감지
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result