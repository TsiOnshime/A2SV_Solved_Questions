# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.common = 0
        def find(root):
            if not root:
                return 
            if q.val >= root.val and p.val <= root.val or p.val >= root.val and q.val <= root.val:
                self.common = root
                return
            if q.val < root.val and p.val < root.val:
                find(root.left)
            else:
                find(root.right)

        find(root)
        return self.common