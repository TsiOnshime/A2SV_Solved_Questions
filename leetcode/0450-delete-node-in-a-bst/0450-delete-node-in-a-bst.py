# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == key:
            temp = root.left
            if root.right:
                prev = root.right
                root = root.right
            else:
                root = root.left
                return root
            while prev.left:
                prev = prev.left
            prev.left = temp
            return root
        curr = root 

        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    temp = curr.left.left
                    if curr.left.right:
                        curr.left = curr.left.right
                    else:
                        curr.left = temp
                        break
                    prev = curr.left
                    while prev.left:
                        prev = prev.left
                    prev.left = temp
                    break
                curr = curr.left
            elif curr.val < key:
                if curr.right and curr.right.val == key:
                    temp = curr.right.left
                    if curr.right.right:
                        curr.right = curr.right.right
                    else:
                        curr.right = temp
                        break
                    prev = curr.right
                    while prev.left:
                        prev = prev.left
                    prev.left = temp
                    break
                curr = curr.right
        return root


        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna