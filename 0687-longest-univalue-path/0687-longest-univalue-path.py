# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def longestPath(root):
            nonlocal max_length
            if not root:
                return [TreeNode(-10000), 0]
            prevleft, leftlength = longestPath(root.left)
            prevright, rightlength = longestPath(root.right)

            if root.val == prevleft.val and root.val == prevright.val:
                max_length = max(max_length, leftlength + rightlength + 2)
                return [root, max(leftlength, rightlength) + 1]
            elif root.val == prevleft.val:
                max_length = max(max_length, leftlength + 1)
                return [root, leftlength + 1]
            elif root.val == prevright.val:
                max_length = max(max_length, rightlength + 1)
                return [root, rightlength + 1]
            else:
                return [root, 0]
        longestPath(root)
        return max_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna