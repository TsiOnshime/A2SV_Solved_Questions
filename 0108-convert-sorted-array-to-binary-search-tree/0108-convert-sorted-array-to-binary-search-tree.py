# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        
        def constructTree(l, r):
            if l >= r:
                return 
            mid = l + (r - l)//2

            root = TreeNode(nums[mid])
            root.left = constructTree(l, mid)
            root.right = constructTree(mid + 1, r)

            return root

        return constructTree(0, len(nums))
# [-10,-3,0,5,9]
# (0, 4)
# mid = 2, root = [0]
# root.left = (0, 2)    root.right = (3, 4)

# mid = 1   root[-3]
# root.left = (0, 1)
# root.right= (2, 2)




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna