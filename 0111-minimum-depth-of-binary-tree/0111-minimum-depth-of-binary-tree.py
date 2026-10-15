# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append([root, 1])

        while queue:
            node, dist = queue.popleft()
            if not node.left and not node.right:
                return dist
            if node.left:
                queue.append([node.left, dist+1])
            if node.right:
                queue.append([node.right, dist+1])
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna