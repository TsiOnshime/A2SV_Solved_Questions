# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(curr, subcurr):
            if not curr and not subcurr:
                return True
            if not curr or not subcurr:
                return False
            
            leftSide = curr.val == subcurr.val and same(curr.left, subcurr.left)
            rightSide = curr.val == subcurr.val and same(curr.right, subcurr.right) 
            return leftSide and rightSide

        def isSubtree(tree, subtree):
            if not subtree:
                return True
            if not tree:
                return False

            return same(tree, subtree) or isSubtree(tree.left, subtree) or isSubtree(tree.right, subtree)

        
        return isSubtree(root, subRoot)

