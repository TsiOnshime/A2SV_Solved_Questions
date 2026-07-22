# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = {val:i for i, val in enumerate(inorder)}

        self.index = len(postorder) - 1
        def build_tree(left, right):
            if left > right or self.index < 0:
                return
            
            root = TreeNode(postorder[self.index])
            self.index -= 1
            mid = self.idx[root.val]
            root.right = build_tree(mid + 1, right)
            root.left = build_tree(left, mid - 1)
        
            return root
        
        return build_tree(0, len(postorder) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna