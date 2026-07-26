# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.middle = None
        self.last = None
        self.prev = TreeNode(float('-inf'))
        def recover(root):
            
            if not root: return
            recover(root.left)
            if self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = root
                else:
                    self.last = root
            self.prev = root
            recover(root.right)

        recover(root)
        if self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna