# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommon(root):
            if not root:
                return 
            left = lowestCommon(root.left)
            right = lowestCommon(root.right)

            if left == None and right == None:
                if root.val == p.val or root.val == q.val:
                    return root
                return 
            elif left != None and right != None:
                return root
            elif left != None:
                if root.val == p.val or root.val == q.val:
                    return root
                return left
            elif right != None:
                if root.val == p.val or root.val == q.val:
                    return root
                return right

        return lowestCommon(root) 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna