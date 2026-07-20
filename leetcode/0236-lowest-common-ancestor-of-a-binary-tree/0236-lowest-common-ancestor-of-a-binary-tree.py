# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lowestAncestor(root):
            if not root:
                return 

            left = lowestAncestor(root.left)
            right = lowestAncestor(root.right)

            if not left and not right:
                if root == p or root == q:
                    return root 
            elif left and right:
                return root
            elif left:
                if root == p or root == q:
                    return root
                return left
            elif right:
                if root == p or root == q:
                    return root
                return right
            

        return lowestAncestor(root)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna