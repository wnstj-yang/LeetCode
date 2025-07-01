class Solution(object):
    def coinChange(self, coins, amount):
        max_amount = amount + 1
        dp = [max_amount] * (amount + 1)
        dp[0] = 0 # 0을 만드려는 동전 개수는 0개
        
        # dp안에는 인덱스가 동전으로 만들 수 있는 amount, 값
        # 각 인덱스의 값은 amount값을 주어진 동전으로 만들 수 있는 최소의 개수이다.
        for coin in coins:
            for num in range(coin, amount + 1):
                dp[num] = min(dp[num], dp[num - coin] + 1)
        if dp[amount] == max_amount:
            return -1
        return dp[amount]

        
        