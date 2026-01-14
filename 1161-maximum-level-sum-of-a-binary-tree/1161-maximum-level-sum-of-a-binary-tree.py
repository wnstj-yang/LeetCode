# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # def __init__(self):
    #     self.total = {}

    # def calculate(self, level, node):
    #     if level not in self.total:
    #         self.total[level] = 0

    #     if node.left is not None:
    #         self.total[level] += node.val
    #     if node.right is not None:
    #         self.total[level] += node.val


    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = [(root, 1)]
        total = {}
        while queue:
            node, now_level = queue.pop(0)
            if node is None:
                continue
            if now_level not in total:
                total[now_level] = 0
            total[now_level] += node.val

            if node.left is not None:
                queue.append((node.left, now_level + 1))
            if node.right is not None:
                queue.append((node.right, now_level + 1))
        result = sorted(total.items(), key=lambda x:-x[1])
        # print(total)
        return result[0][0]

        
        