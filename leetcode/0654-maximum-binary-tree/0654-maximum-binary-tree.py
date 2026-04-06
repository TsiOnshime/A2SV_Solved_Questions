# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None

        def dfs(start, end):

            if start > end:
                return None

            idxMax = start

            for i in range(start + 1, end + 1):
                if nums[i] > nums[idxMax]:
                    idxMax = i
            
            root = TreeNode(nums[idxMax])

            root.left = dfs(start, idxMax - 1)
            root.right = dfs(idxMax + 1, end)

            return root

            
        return dfs(0, len(nums) - 1)