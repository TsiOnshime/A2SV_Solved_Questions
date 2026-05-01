# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        level = 0
        queue.append([root, level])

        while queue:
            node, level = queue.popleft()
            for neigh in [node.left, node.right]:
                if neigh:
                    queue.append([neigh, level + 1])

        
        return level + 1
