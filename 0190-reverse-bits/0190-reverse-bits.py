class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_list = [0] * 32
        idx = 31
        while idx > 0:
            if n % 2 == 1: # 나머지 값이 1이면 해당 위치 이진수 값이 필요함 (Ex. 값(나머지연산 이진수) 6(0) -> 3(1) -> 1(1) : 110))
                binary_list[idx] = 1
            n //= 2
            idx -= 1

        binary_list.reverse() # 뒤집기
        result = 0 # 결과물
        binary = 1 # 현재 위치의 이진수 값
        for i in range(31, -1, -1):
            if binary_list[i] == 1:
                result += binary
            binary *= 2
        return result
        