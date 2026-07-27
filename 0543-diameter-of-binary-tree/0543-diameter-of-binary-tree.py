# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def diameter(root):
            if not root:
                return 0
            
            leftDiameter = diameter(root.left)
            rightDiameter = diameter(root.right)

            self.max_diameter = max(self.max_diameter, leftDiameter + rightDiameter)

            return 1 + max(leftDiameter, rightDiameter)

        diameter(root)
        return self.max_diameter

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna