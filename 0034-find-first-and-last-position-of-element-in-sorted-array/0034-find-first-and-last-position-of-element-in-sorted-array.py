class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(self, left_side):
            left, right = 0, len(nums) - 1
            result = -1 # 초기 리턴 값을 -1로 설정(없는 경우 -1)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # 같기 때문에 같은 인덱스는 추가하고 아래는 왼쪽, 오른쪽의 같은 인덱스가 있는 경우 탐색 지속 진행
                    result = mid
                    if left_side:
                        right = mid - 1
                    else:
                        left = mid + 1
            return result

        answer = [-1, -1]
        answer[0] = binary_search(self, True)
        answer[1] = binary_search(self, False)
        
        return answer

        
        