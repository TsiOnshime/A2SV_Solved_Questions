# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        queue = deque()
        queue.append([root, 0])

        while queue:
            min_idx = queue[0][1]
            max_idx = queue[-1][1]
            max_width = max(max_width, max_idx - min_idx + 1)
            n = len(queue)
            for i in range(n):
                node, idx = queue.popleft()
                index = idx - min_idx
                if node.left:
                    queue.append([node.left, 2 * index + 1])
                if node.right:
                    queue.append([node.right, 2 * index + 2])
        return max_width


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna