class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            direction = nums[i] > 0

            while True:
                # slow 한 칸
                next_slow = self.next_index(nums, slow)

                # fast 두 칸
                next_fast = self.next_index(nums, fast)
                if next_fast != -1:
                    next_fast = self.next_index(nums, next_fast)

                # 방향 다르면 종료
                if next_slow == -1 or next_fast == -1:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    return True

            # 방문 처리 (0으로 만들어서 재탐색 방지)
            j = i
            while nums[j] != 0:
                next_j = self.next_index(nums, j)
                nums[j] = 0
                if next_j == -1:
                    break
                j = next_j

        return False

    def next_index(self, nums, i):
        n = len(nums)
        direction = nums[i] > 0
        next_i = (i + nums[i]) % n

        # 자기 자신 루프 제거
        if next_i == i:
            return -1

        # 방향 체크
        if (nums[next_i] > 0) != direction:
            return -1

        return next_i