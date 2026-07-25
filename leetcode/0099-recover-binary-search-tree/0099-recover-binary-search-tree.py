# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp1 = TreeNode(float('inf'))
        temp2 = TreeNode(float('-inf'))
        
        def recoverBst(lowerBound, upperBound, upperCurr, lowerCurr, root):
            nonlocal flag
            if not root:
                return 
            if root.val >= upperBound:
                root.val, upperCurr.val = upperCurr.val, root.val
                flag = True
                return 
            elif root.val <= lowerBound:
                root.val, lowerCurr.val = lowerCurr.val, root.val
                flag = True
                return 
            recoverBst(lowerBound, root.val, root, lowerCurr, root.left)
            recoverBst(root.val, upperBound, upperCurr, root, root.right)
        while True:
            flag = False
            recoverBst(float('-inf'), float('inf'), temp1, temp2, root)
            if not flag:
                break

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna