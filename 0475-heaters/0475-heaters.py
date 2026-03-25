class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        # 1 2 3 4 5 6 7 8 9 50
        # 히터 -> 5, 30
        # 5인경우 왼쪽으로 4, 오른쪽으로 45 범위 필요
        # 30인 경우 왼쪽으로 29, 오른쪽으로 20 범위 필요
        houses.sort()
        heaters.sort()
        result = 0
        # 시간초과 발생 
        # for house in houses:
        #     min_dist = int(1e9) + 1

        #     for heater in heaters:
        #         dist = abs(house - heater)
        #         min_dist = min(min_dist, dist)

        #     # 그 중 최댓값
        #     result = max(result, min_dist)
        # return result

        # 이분탐색을 통해서 집과 가까운 히터를 찾는다
        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid

            # left가 "오른쪽 heater" 위치
            right_dist = abs(heaters[left] - house)

            # 왼쪽 heater 거리도 비교
            left_dist = float('inf')
            if left > 0:
                left_dist = abs(heaters[left - 1] - house)

            # 가장 가까운 heater 선택
            nearest = min(left_dist, right_dist)

            result = max(result, nearest)
        return result




        # houses.sort()
        # heaters.sort()
        # left, right = 0, len(heaters) - 1
        # h_min, h_max = houses[0], houses[len(houses) - 1]
        # ans = 987654321
        # while left < right:
        #     # 기준 세우기
        #     mid = (left + right) // 2
        #     min_diff = abs(heaters[mid] - h_min)
        #     max_diff = abs(heaters[mid] - h_max)
        #     print(min_diff, max_diff)
        #     if min_diff < max_diff:
        #         left += 1
        #         ans = max_diff
        #     else:
        #         right += 1
        #         ans = min_diff
        # print(ans)
        


        