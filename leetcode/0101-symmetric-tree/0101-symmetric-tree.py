# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def symmetric(root1, root2):
            if not root1 or not root2:
                return root1 == root2
            if root1.val != root2.val:
                return False
            
            return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
        
        return symmetric(root.left, root.right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna