# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')


        def recurse(curr):
            nonlocal res

            if not curr:
                return 0
            
            leftChild = recurse(curr.left)
            rightChild = recurse(curr.right)

            res = max(res, curr.val + max(leftChild, 0) + max(rightChild, 0))

            return max(curr.val, curr.val + max(leftChild, rightChild))

        recurse(root)
        return res