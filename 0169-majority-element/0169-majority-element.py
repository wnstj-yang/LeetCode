class Solution(object):
    def majorityElement(self, nums):
        ans = 0
        nums_cnt = {}
        for num in nums:
            if num not in nums_cnt:
                nums_cnt[num] = 1
            else:
                nums_cnt[num] += 1
            if nums_cnt[num] > len(nums) // 2:
                return num
                