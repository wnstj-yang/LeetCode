# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def sumNumbers(self, root):
#         global ans # 맞긴하나 설계상 이점은 아님. 전역변수라는 것이 변경될 수도 있기 때문
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         ans = 0
#         def dfs(node, result):
#             global ans

#             if node is None:
#                 return
#             if node.left is None and node.right is None:
#                 ans += int(result + str(node.val))
#                 return

#             dfs(node.left, result + str(node.val))
#             dfs(node.right, result + str(node.val))
#         dfs(root, '')
#         return ans


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, result):
            if node is None:
                return 0
                
            result = result * 10 + node.val
            if node.left is None and node.right is None:
                return result

            return dfs(node.left, result) + dfs(node.right, result)

        return dfs(root, 0)
        