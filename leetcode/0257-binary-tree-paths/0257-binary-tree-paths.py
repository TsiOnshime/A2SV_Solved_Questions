# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def binaryPath(root, path):
            nonlocal res
            if not root.left and not root.right:
                path.append(str(root.val))
                if len(path) >= 2:
                    res.append("->".join(path))
                elif len(path) == 1:
                    res.append("".join(path))
                return 
            
            path.append(str(root.val))
            if root.left:
                binaryPath(root.left, path)
                path.pop()
            if root.right:
                binaryPath(root.right, path)
                path.pop()
        binaryPath(root, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna