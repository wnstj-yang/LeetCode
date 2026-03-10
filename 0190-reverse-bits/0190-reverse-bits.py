class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_list = [0] * 32
        idx = 31
        while idx > 0:
            if n % 2 == 1:
                binary_list[idx] = 1
            n //= 2
            idx -= 1

        binary_list.reverse()
        # print(binary_list)
        result = 0
        binary = 1
        for i in range(31, -1, -1):
            if binary_list[i] == 1:
                result += binary
            binary *= 2
        return result
        # result = 0
        # for _ in range(32):
        #     print(result, n % 2, n)
        #     result = result * 2 + (n % 2)
        #     n = n // 2
        # print(result)
        