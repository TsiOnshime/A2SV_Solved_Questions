# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(root):
            if not root:
                return [True, 0]
            
            left = checkBalance(root.left)
            right = checkBalance(root.right)

            if not left[0] or not right[0]:            
                return [False, 1 + max(left[1], right[1])]
            balanced = abs(left[1] - right[1]) <= 1
            if balanced:
                return [True, 1 + max(left[1], right[1])]
            else:
                return [False, 1 + max(left[1], right[1])]
        return checkBalance(root)[0]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna