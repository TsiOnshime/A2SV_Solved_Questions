# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(curr, currSum):
            if not curr:
                return False
            
            currSum += curr.val
            if not curr.right and not curr.left:
                return currSum == targetSum
                
            leftSum = pathSum(curr.left, currSum)
            rightSum = pathSum(curr.right, currSum)

            return leftSum or rightSum

        return pathSum(root, 0)