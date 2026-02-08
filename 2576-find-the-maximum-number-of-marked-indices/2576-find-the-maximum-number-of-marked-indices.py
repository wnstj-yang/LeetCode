class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1. 인덱스를 한 번만 사용할 수 있다
        # 2. 겹치면 안된다
        # 3. 1, 2 조건 + 쌍이기 때문에 정렬하고 left는 0, right는 len(nums) // 2 시작
        # 4. 쌍으로 구하는 것이라 2씩 더하면 될듯
        if len(nums) < 2:
            return 0
        nums.sort()
        left, right = 0, 1
        ans = 0

        while left < len(nums) // 2 and right < len(nums):
            if nums[left] * 2 <= nums[right]:
                left += 1
                right += 1 # 이미 선택한 인덱스이기에 같이 1을 추가해주면서 진행한다
                ans += 2
            # 조건에 안맞으면 right의 값이 작은 것이기 때문에 큰 것을 찾아 떠난다
            else:
                right += 1
        return ans