class Solution(object):
    def superPow(self, a, b):
        result = 1
        p = int(''.join([str(num) for num in b]))
        return pow(a, p, 1337)
        