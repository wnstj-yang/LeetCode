class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = 0
        num1_10 = 10 ** 0
        for n1 in num1:
            int_n1 = int(n1) * num1_10
            num2_10 = 10 ** 0
            num = 0
            for n2 in num2:
                int_n2 = int(n2) * num2_10 * int_n1
                num += int_n2
                num2_10 *= 10
            result += num
            num1_10 *= 10
        return str(result)
        