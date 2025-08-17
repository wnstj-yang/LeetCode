# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = {}
        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if level not in result:
                result[level] = [node.val]
            else:
                result[level].append(node.val)
            if node.left is not None:
                queue.append((level + 1, node.left))
            if node.right is not None:
                queue.append((level + 1, node.right))
        return result.values()

