class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0] # 첫 시작 값
        dp[1] = max(dp[0], nums[1]) # 두 번째에서 시작하면 이전과 최댓값 비교

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # MAX(이전 까지의 최대 값, 방범건너뛰기 위해 2개 이전 최대값 + 현재 값)
        return dp[-1] # 끝까지 진행하며 얻은 최대값 -> 마지막
