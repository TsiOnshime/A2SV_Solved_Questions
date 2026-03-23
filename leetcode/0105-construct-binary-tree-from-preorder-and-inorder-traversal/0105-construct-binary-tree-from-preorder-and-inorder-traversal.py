# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def tree(preorder, inorder):
            # check if we're at a leaf node
            if not preorder or not inorder:
                return None


            # get the parent node
            parent = preorder[0]
            # initialize our node
            binary_tree = TreeNode(parent)
            # get the indext in which the left subtree and right subtree split for that particular parent node
            mid = inorder.index(parent)

            binary_tree.left = tree(preorder[1:mid + 1], inorder[:mid + 1])
            binary_tree.right = tree(preorder[mid + 1:], inorder[mid + 1:])

            return binary_tree
        
        return tree(preorder, inorder)
            