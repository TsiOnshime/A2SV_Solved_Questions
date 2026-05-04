# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue1 = deque([root.left])
        queue2 = deque([root.right])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            for neigh in [node1.left, node1.right]:
                queue1.append(neigh)
            for neigh in [node2.right, node2.left]:
                queue2.append(neigh)
            
        if len(queue1) != len(queue2):
            return False

        return True