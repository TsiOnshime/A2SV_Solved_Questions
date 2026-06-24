# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(lambda:defaultdict(list))
    
        def dfs(root, r, c):
            nonlocal order
            if not root:
                return 
           
            order[c][r].append(root.val)
            dfs(root.left, r + 1, c - 1)
            dfs(root.right, r + 1, c + 1)
        
        dfs(root, 0, 0)

        res = []

        for col in sorted(order):
            r = []
            for row in sorted(order[col]):
                r.extend(sorted(order[col][row]))
            res.append(r)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna