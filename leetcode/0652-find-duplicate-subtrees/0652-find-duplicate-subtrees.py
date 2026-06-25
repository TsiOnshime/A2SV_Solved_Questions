# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        node_count = defaultdict(int)

        def dfs(root):
            if not root:
                return "null"

            node = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
            if node_count[node] == 1:
                res.append(root)
            node_count[node] += 1
            return node
        dfs(root)
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna