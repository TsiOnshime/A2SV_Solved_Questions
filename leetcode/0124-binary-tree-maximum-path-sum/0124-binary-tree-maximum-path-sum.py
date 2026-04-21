# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.Max = float('-inf')

        def dfs(curr):

            if not curr:
                return 0

            leftSum = max(dfs(curr.left), 0)
            rightSum = max(dfs(curr.right), 0)

            self.Max = max(self.Max, leftSum + curr.val + rightSum)

            return curr.val + max(leftSum, rightSum)

        dfs(root)
        return self.Max

