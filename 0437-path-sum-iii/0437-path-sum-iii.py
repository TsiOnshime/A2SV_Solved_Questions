# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count = 0
        pSums = defaultdict(int)
        pSums[0] = 1

        def path(curr, prevSum):

            if not curr:
                return 
            
            currSum = curr.val + prevSum

            x = currSum - targetSum

            if x in pSums:
                self.count += pSums[x]
            pSums[currSum] += 1

            path(curr.left, currSum)
            path(curr.right, currSum)
            pSums[currSum] -= 1


        path(root, 0)
        return self.count


