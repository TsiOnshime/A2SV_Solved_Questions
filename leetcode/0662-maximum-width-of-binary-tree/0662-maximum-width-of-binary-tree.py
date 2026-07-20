# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # level: [verticals] [0]
        max_width = 1
        hashmap = defaultdict(list)

        def maxWidth(root, level, index):
            nonlocal hashmap
            if not root:
                return 
            hashmap[level].append(index)
            maxWidth(root.left, level + 1, 2 * index + 1)
            maxWidth(root.right, level + 1, 2 * index + 2)
        maxWidth(root, 0, 0)
        for key, val in hashmap.items():
            first = val[0]
            second = val[-1]
            max_width = max(max_width, second - first + 1)
        
        return max_width
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna