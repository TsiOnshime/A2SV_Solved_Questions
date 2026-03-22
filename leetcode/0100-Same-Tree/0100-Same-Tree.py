# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(curr1, curr2):
            if curr1 == None and curr2 == None:
                return True
            elif curr1 == None:
                return False
            elif curr2 == None:
                return False
            

            
            leftSide = curr1.val == curr2.val and same(curr1.left, curr2.left) 
            rightSide = curr1.val == curr2.val and same(curr1.right, curr2.right) 
            
            return leftSide & rightSide

        return same(p, q)