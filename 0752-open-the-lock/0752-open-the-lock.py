from collections import deque

class Solution:
    def openLock(self, deadends, target):

        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        visited = {"0000"}

        queue = deque([("0000", 0)])

        while queue:
            number, cnt = queue.popleft()

            if number == target:
                return cnt

            for i in range(4):
                num = int(number[i])

                for add in (1, -1):

                    new_number = (
                        number[:i]
                        + str((num + add) % 10)
                        + number[i + 1:]
                    )

                    if (
                        new_number not in visited
                        and new_number not in deadends
                    ):
                        visited.add(new_number)
                        queue.append((new_number, cnt + 1))

        return -1