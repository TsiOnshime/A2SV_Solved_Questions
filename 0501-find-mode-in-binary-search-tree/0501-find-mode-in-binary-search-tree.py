# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        count = 1
        maxCount = 1
        modes = set()
        prev = None

        def inorder(node, modes):
            nonlocal count
            nonlocal maxCount
            nonlocal prev
           
            if not node:
                return 

            inorder(node.left, modes)
            if prev != None:
                if prev.val == node.val:
                    count += 1
                else:
                    count = 1
            if count > maxCount:
                maxCount = count
                modes.clear()
                modes.add(node.val)
            elif count == maxCount:
                modes.add(node.val)

            prev = node

            inorder(node.right, modes)
        
        inorder(root, modes)

        return list(modes)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna