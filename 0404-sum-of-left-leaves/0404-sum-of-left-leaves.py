# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        _sum = 0

        def find_sum(root, left):
            nonlocal _sum
            if not root:
                return 
            if not root.left and not root.right:
                if left:
                    _sum += root.val
                else:
                    return 
            find_sum(root.left, True)
            find_sum(root.right, False)
            
       
            

        find_sum(root, False)
        return _sum

        


            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna