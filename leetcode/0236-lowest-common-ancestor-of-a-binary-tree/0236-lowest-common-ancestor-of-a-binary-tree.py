# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.commonAncestor = None

        def lowestCommon(root):
            if not root:
                # found, ancestor
                return False
            
            left = lowestCommon(root.left)
            right = lowestCommon(root.right)

            if not left and not right:
                if root.val == q.val or root.val == p.val:
                    return True
                return False

            if left and right:
                if self.commonAncestor is None:
                    self.commonAncestor = root
                return True
            
            if left:
                if root.val == p.val or root.val == q.val:
                    if self.commonAncestor is None:
                        self.commonAncestor = root
                return True
            if right:
                if root.val == p.val or root.val == q.val:
                    if self.commonAncestor is None:
                        self.commonAncestor = root
                return True
            return False

        lowestCommon(root)
        return self.commonAncestor

                


            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna