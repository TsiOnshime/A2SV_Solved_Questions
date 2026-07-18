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
        queue.append([root, 1])
        max_depth = 1
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for neigh in [node.left, node.right]:
                if neigh:
                    queue.append([neigh, depth + 1])
        return max_depth


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna