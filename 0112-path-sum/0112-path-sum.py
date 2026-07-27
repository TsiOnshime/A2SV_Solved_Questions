# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def checkPathSum(root, _sum):
            if not root:
                return False
            if not root.left and not root.right:
                if _sum + root.val == targetSum:
                    return True
                return False

            return checkPathSum(root.left, _sum + root.val) or checkPathSum(root.right, _sum + root.val)

        
        return checkPathSum(root, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna