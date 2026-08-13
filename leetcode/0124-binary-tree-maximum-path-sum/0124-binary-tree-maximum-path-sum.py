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
            
            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))

            max_sum = max(root.val + left + right, max_sum)
            return max(left, right) + root.val


        pathSum(root)

        return max_sum




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna