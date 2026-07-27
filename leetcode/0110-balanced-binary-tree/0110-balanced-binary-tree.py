# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def is_balanced(root):
            if not root:
                return [True, 0]

            leftBalanced = is_balanced(root.left)
            rightBalanced = is_balanced(root.right)

            if not leftBalanced[0] or not rightBalanced[0]:
                return [False, max(leftBalanced[1], rightBalanced[1])]
            balance = abs(leftBalanced[1] - rightBalanced[1])

            if balance <= 1:
                return [True, 1 + max(leftBalanced[1], rightBalanced[1])]
            
            return [False, max(leftBalanced[1], rightBalanced[1])]
        return is_balanced(root)[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna