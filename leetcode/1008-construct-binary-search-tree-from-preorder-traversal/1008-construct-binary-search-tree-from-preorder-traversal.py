# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def insertNode(root, val):
            node = TreeNode(val)
            curr = root
            while curr:
                if node.val < curr.val:
                    if not curr.left:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                else:
                    if not curr.right:
                        curr.right = node
                        break
                    else:
                        curr = curr.right
        
        for i in range(1, len(preorder)):
            insertNode(root, preorder[i])
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna