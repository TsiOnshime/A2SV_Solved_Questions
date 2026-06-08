# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            if stack:
                curr.right = stack[-1]
            curr.left = None

        
# [1]
# curr = 1, stack = [5, 2]
# 
#


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna