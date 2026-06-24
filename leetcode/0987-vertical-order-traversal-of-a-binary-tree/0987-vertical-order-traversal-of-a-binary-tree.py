# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(lambda:defaultdict(list))
        queue = deque()
        
        queue.append([root, 0, 0])
        while queue:
            node, r, c = queue.popleft()
            order[c][r].append(node.val)
            if node.left:
                queue.append([node.left, r + 1, c - 1])
            if node.right:
                queue.append([node.right, r + 1, c + 1])


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