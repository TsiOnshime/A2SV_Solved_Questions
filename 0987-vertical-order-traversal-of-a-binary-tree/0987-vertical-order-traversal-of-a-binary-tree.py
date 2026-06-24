# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        queue = deque()
        
        queue.append([root, 0, 0])
        while queue:
            node, r, c = queue.popleft()
            nodes.append([c, r, node.val])
            if node.left:
                queue.append([node.left, r + 1, c - 1])
            if node.right:
                queue.append([node.right, r + 1, c + 1])

        nodes.sort()
        res = [[]]

        last_col = nodes[0][0]
        for i in range(len(nodes)):
            c, r, val = nodes[i]
            if c == last_col:
                res[-1].append(val)
            else:
                res.append([val])
                last_col = c
        return res
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna