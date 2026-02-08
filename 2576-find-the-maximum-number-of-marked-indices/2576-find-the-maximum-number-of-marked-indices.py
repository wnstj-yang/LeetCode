class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        left, right = 0, len(nums) // 2
        ans = 0
        # print(nums)
        while left < len(nums) // 2 and right < len(nums):
            # print(left, right, nums[left] * 2, ' <= ', nums[right])
            if nums[left] * 2 <= nums[right]:
                left += 1
                right += 1
                ans += 2
            else:
                right += 1
        return ans