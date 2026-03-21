# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._sum = 0 
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def pathSum(curr, parent, grandparent):
            if curr == None:
                return

            if grandparent and grandparent.val % 2 == 0:
                self._sum += curr.val
            
            if curr.left:
                pathSum(curr.left, curr, parent)
            if curr.right:
                pathSum(curr.right, curr, parent)
        
        pathSum(root, None, None)
        return self._sum
        
# call stack

"""
|                               |          _sum = 2 + 7 + 1 + 3 + 5 = 18
|                               |
|                               |
|                              |
|                   |
|                    |
|                             |
"""