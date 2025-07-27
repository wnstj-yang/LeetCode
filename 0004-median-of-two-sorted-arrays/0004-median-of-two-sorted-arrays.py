class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        mid = len(nums) // 2
        ans = nums[mid]
        if len(nums) % 2 == 0:
            ans += nums[mid - 1]
            ans /= 2.0
        # print("{:.5f}".format(ans))
        return ans
        