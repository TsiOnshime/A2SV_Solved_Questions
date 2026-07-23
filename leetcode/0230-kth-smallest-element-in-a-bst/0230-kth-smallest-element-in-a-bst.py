# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder = []
        curr = root
        while curr:
            if not curr.left:
                inorder.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right: 
                    temp.right = curr
                    curr = curr.left
                elif temp.right == curr:
                    inorder.append(curr.val)
                    temp.right = None
                    curr = curr.right
        
        return inorder[k - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna