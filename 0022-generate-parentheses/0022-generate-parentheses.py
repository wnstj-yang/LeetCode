class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def dfs(l, r, result):
            if l < r:
                return
            if l == n and r == n:
                ans.append(result)
                return
            if l < n:
                dfs(l + 1, r, result + '(')
            if r < n:
                dfs(l, r + 1, result + ')')
        dfs(0, 0, '')
        return ans
        