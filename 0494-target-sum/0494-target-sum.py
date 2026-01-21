class Solution(object):

    def findTargetSumWays(self, nums, target):
        ans = {}
        # 단순 재귀할 시 중복을 많이 들려서 시간초과 발생
        # 중복 방지를 위해 메모이제이션 적용
        def check_sum(idx, result):
            if idx == len(nums):
                return 1 if target == result else 0
            
            # 현재까지 재귀가 왔을 때 이미 계산된 값이면 반환
            if (idx, result) in ans:
                return ans[(idx, result)]

            minus = check_sum(idx + 1, result - nums[idx])
            plus = check_sum(idx + 1, result + nums[idx])

            # (현재 인덱스, 현재 총합) 기준의 key와 그에 대한 target이 만들어진 경우의 수를 저장 및 반환
            ans[(idx, result)] = plus + minus
            return ans[(idx, result)]

        return check_sum(0, 0)
