# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def pathSum(root):
            nonlocal max_sum
            if not root:
                return 0
            leftSum = pathSum(root.left)
            rightSum = pathSum(root.right)
            
            max_sum = max(max_sum, root.val + leftSum + rightSum)
            if root.val + max(leftSum, rightSum) < 0:
                return 0
            return root.val + max(leftSum, rightSum)
        
        pathSum(root)
        return max_sum



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna