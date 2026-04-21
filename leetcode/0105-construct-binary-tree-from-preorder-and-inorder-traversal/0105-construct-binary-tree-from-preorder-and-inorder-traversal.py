# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.val_idx = {val:i for i, val in enumerate(inorder)}

        self.idx = 0

        def build(left, right):
            if left > right:
                return

            root = TreeNode(preorder[self.idx])
            self.idx += 1
            mid = self.val_idx[root.val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(preorder) - 1)