"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        hashMap = defaultdict(list)

        def dfs(root, level):
            if not root:
                return
            
            if hashMap[level]:
                root.next = hashMap[level][-1]
            
            hashMap[level].append(root)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna