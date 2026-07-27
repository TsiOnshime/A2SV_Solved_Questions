# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def findPath(root, _sum, path):
            if not root:
                return 

            path.append(root.val)
            _sum += root.val
            if not root.left and not root.right:
                if _sum == targetSum:
                    res.append(path.copy())
                 
            else:  
                findPath(root.left, _sum, path)
                findPath(root.right, _sum, path)
            path.pop()
        
        findPath(root, 0, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna