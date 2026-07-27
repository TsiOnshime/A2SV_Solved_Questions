# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        def maxSum(root):
            if not root:
                return 0
            leftSum = maxSum(root.left)
            rightSum = maxSum(root.right)

            left = max(leftSum, 0)
            right = max(rightSum, 0)

            self.max_path_sum = max(self.max_path_sum, root.val + left + right)

            return root.val + max(left, right)

        maxSum(root)
        return self.max_path_sum



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna