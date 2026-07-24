# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        def constructBst(upperBound):
            nonlocal idx
            if idx == len(preorder):
                return 
            if preorder[idx] > upperBound:
                return 
            root = TreeNode(preorder[idx])
            idx += 1
            root.left = constructBst(root.val)
            root.right = constructBst(upperBound)

            return root
        return constructBst(float('inf'))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna