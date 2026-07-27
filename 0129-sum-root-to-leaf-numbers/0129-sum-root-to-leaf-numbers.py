# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        def sum_numbers(root, _sum):
            if not root:
                return 
            _sum = _sum * 10 + root.val
            if not root.right and not root.left:
                self.total_sum += _sum
                return 
            sum_numbers(root.left, _sum)
            sum_numbers(root.right, _sum)  

        sum_numbers(root, 0)
        return self.total_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna