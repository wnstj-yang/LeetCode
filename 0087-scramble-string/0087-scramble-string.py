class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}
        
        def dfs(a, b):
            # 1. 메모 확인
            if (a, b) in memo:
                return memo[(a, b)]
            
            # 2. 같으면 True
            if a == b:
                memo[(a, b)] = True
                return True
            
            # 3. 문자 구성 다르면 False (가지치기)
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            
            # 4. 분할 시도
            for i in range(1, n):
                
                # (1) swap 안함
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                
                # (2) swap 함
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return dfs(s1, s2)