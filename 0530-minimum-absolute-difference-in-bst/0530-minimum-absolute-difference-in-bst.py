# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        _min = float('inf')
        prev = float('-inf')
        def find_min(root):

            nonlocal _min, prev
            if not root:
                return 
            
            find_min(root.left)
            _min = min(_min, root.val - prev)
            prev = root.val
            find_min(root.right)
        
        find_min(root)
        return _min

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna