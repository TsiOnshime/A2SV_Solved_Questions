# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root: return None
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == None and right == None:
                if root == p or root== q:
                    return root
                else:
                    return None
            elif left != None and right != None:
                return root
            
            elif left != None and right == None:
                if root == p or root == q:
                    return root
                else:
                    return left
            elif left == None and right != None:
                if root == p or root== q:
                    return root
                return right
        return dfs(root)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna