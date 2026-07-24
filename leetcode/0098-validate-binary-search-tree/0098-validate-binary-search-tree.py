# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, left, right):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            
            validateLeft = validate(root.left, left, root.val)
            validateRight = validate(root.right, root.val, right)

            return validateLeft and validateRight

        

        return validate(root, float('-inf'), float('inf'))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna