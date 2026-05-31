# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        queue = deque()
        queue.append([root, 0])
        r = l = 0
        offset = 0

        while queue:
            Found = False
            n = len(queue)
            for _ in range(n):
                node, idx = queue.popleft()
                if _ == 0:
                    l = idx
                if _ == n - 1:
                    r = idx
                if not Found:
                    offset = idx
                    Found = True
                if node.left:
                    i = (idx - offset) * 2 + 1
                    queue.append([node.left, i])
                if node.right:
                    i = (idx - offset) * 2 + 2
                    queue.append([node.right, i])
            max_width = max(max_width, r - l + 1)
        
        return max_width
                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna