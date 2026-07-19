# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def find_tilt(root):
            nonlocal _sum
            if not root: return 0

            left = find_tilt(root.left)
            right = find_tilt(root.right)
            _sum += abs(left - right)
            return root.val + left + right
        find_tilt(root)
        return _sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna