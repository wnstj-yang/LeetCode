class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        # for i in range(len(temperatures) - 1):
        #     cnt = 1
        #     left = temperatures[i]
        #     for j in range(i + 1, len(temperatures)):
        #         if left < temperatures[j]:
        #             result[i] = cnt
        #             break
        #         cnt += 1
        # stack 방식
        # stack에 넣을 값(temperature)보다 top에 있는 temp값이 작으면
        # 문제에서 더 따듯한 온도를 가지게 되므로 pop 후 해당 tareget_index에 현재 index값으로 뺀다.
        # 그럼 그 자리에 몇 칸 가야 따듯해지는지 알 수 있다.
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                target_index, temp = stack.pop()
                result[target_index] = index - target_index
            stack.append((index, temperature))
        return result
