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
        r = l = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node, idx = queue.popleft()
                if i == 0:
                    l = idx
                elif i == n - 1:
                    r = idx
                
                if node.left:
                    queue.append([node.left, 2 * idx + 1])
                if node.right:
                    queue.append([node.right, 2 * idx + 2])

            max_width = max(max_width, r - l + 1)

        return max_width


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna