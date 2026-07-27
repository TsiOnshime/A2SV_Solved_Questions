# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        def countPathSum(root, currSum):
            if not root:
                return
            currSum += root.val
            complement = currSum - targetSum
            if sum_count[complement] != 0:
                self.count += sum_count[complement]
            
            sum_count[currSum] += 1

            countPathSum(root.left, currSum)
            countPathSum(root.right, currSum)
            
            sum_count[currSum] -= 1
        
        countPathSum(root, 0)
        return self.count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna