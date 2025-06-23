class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1. 단순 pop and insert => 시간 초과 발생 
        # k = k % len(nums)
        # for _ in range(k):
        #     nums.insert(0, nums.pop())
        ##########################################
        
        # 2. 나머지 연산을 통한 k값을 기준으로 붙여넣기
        k = k % len(nums)
        n = len(nums) - k
        # k를 기준으로 앞과 뒤에 새로 붙여주는 리스트들을 교환
        nums[:k], nums[k:] = nums[-k:], nums[:n]
            