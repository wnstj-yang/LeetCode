class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def dfs(l, r, result):
            # l보다 r이 크게되면 짝궁이 만들어지지 않기에 return
            # Ex. (()( 식으로 됨
            if l < r:
                return
            # dfs를 돌면서 양쪽 모두 같은 경우 정답 리스트에 추가
            if l == n and r == n:
                ans.append(result)
                return
            # 끝에 추가를 해야 괄호 짝궁이 만들어짐
            if l < n:
                dfs(l + 1, r, result + '(')
            if r < n:
                dfs(l, r + 1, result + ')')
        dfs(0, 0, '')
        return ans
        