# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftBound, rightBound = float('-inf'), float('inf')
        queue = deque()
        queue.append([root, leftBound, rightBound])

        while queue:
            node, left, right = queue.popleft()

            if node.val <= left or node.val >= right:
                return False
            
            if node.left:
                queue.append([node.left, left, node.val])
            if node.right:
                queue.append([node.right, node.val, right])

        
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna