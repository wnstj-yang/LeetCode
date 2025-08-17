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
        result = {}
        queue = [(0, root)] # 큐를 활용하여 순회한다.(트리의 형태만 갖춰짐)
        while queue:
            level, node = queue.pop(0)
            if not node: # 비어있으면 끝
                break
            # 같은 레벨 선상의 key가 없으면 생성, 있으면 값 추가
            if level not in result:
                result[level] = [node.val]
            else:
                result[level].append(node.val)
            # 각 노드의 왼쪽과 오른쪽 순서대로 체크해서 다음 단계가 존재하므로 level 증가 및 다음 노드 큐에 추가
            if node.left is not None:
                queue.append((level + 1, node.left))
            if node.right is not None:
                queue.append((level + 1, node.right))
        return result.values()

