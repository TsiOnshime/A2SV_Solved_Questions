# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        order = []
        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                for neigh in [node.left, node.right]:
                    if neigh:
                        queue.append(neigh)
                if i == n - 1:
                    order.append(node.val)

        return order

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna