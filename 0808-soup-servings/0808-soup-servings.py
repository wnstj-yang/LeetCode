class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # 재귀를 돌아야한다. 다만, A를 기준으로 해야함. 즉, A가 먼저 없어지는 경우의 확률 찾기
        def recursive(a, b, memo):
            # 1. A가 남아있지 않으면 끝
            if a <= 0 and b > 0:
                return 1.0
            # 2. A와 B 모두 남아있지 않거나 초과하여 남아있지않을 때 1/2
            elif a <= 0 and b <= 0:
                return 0.5
            # 3. A가 여전히 남아있는 경우
            elif a > 0 and b <= 0:
                return 0.0
            # 재귀를 돌수록 중복되는 부분을 대처하고자함
            if memo[a][b] != -1:
                return memo[a][b]                
            
            first = 0.25 * recursive(a - 100, b, memo)
            second = 0.25 * recursive(a - 75, b - 25, memo)
            third = 0.25 * recursive(a - 50, b - 50, memo)        
            fourth = 0.25 * recursive(a - 25, b - 75, memo)
            memo[a][b] = first + second + third + fourth
            return memo[a][b]
        # n이 커질수록 결국 확률을 더하면서 1에 가까워지는데, 조건에 10^-5에 대한 오차는 허용하므로
        # n이 4800정도되면 0.99999임. 그래서 4800보다 크면 1.0으로 수렴하여 반환
        if n > 4800:
            return 1.0
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return recursive(n, n, memo)