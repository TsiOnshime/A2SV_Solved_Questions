# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.index = {val: i for i, val in enumerate(inorder)}
        self.idx = 0
        def build_tree(left, right):
            if left > right:
                return

            root = TreeNode(preorder[self.idx])
            self.idx += 1
            mid = self.index[root.val]
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)

            return root
        return build_tree(0, len(preorder) - 1)




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna