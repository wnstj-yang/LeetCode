class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}
        # test = [1, 2, 3]
        # print(test[:0], test[0:])

        def dfs(a, b):
            # 이미 체크한 적이 있으면 반환
            if (a, b) in memo:
                return memo[(a, b)]
            # 둘이 같으면 scramble 성공
            if a == b:
                memo[(a, b)] = True
                return True
            # 다른 경우(구성자체가 scramble할 수 없는 경우를 체크함)
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            length = len(a)

            # 빈 값이 되면 안됨, a를 기준으로
            for i in range(1, length):
                # 1. swap을 하지 않는다
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # 2. swap을 한다.
                if dfs(a[:i], b[length - i:]) and dfs(a[i:], b[:length-i]):
                    memo[(a, b)] = True
                    return True

            # 해당안하면 끝
            memo[(a, b)] = False
            return False
        return dfs(s1, s2)
