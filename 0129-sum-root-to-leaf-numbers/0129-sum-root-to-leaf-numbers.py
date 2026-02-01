# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        global ans
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0
        def dfs(node, result):
            global ans
            if node is None:
                return
            if node.left is None and node.right is None:
                ans += int(result + str(node.val))
                return
            # if node.right is None:
            #     ans += int(result + str(node.val))
            #     return

            dfs(node.left, result + str(node.val))
            dfs(node.right, result + str(node.val))
        dfs(root, '')
        return ans
        