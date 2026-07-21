# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def FindLeftHeight(root):
            height = 1
            curr = root
            while curr:
                curr = curr.left
                height += 1
            return height
        
        def FindRightHeight(root):
            height = 0
            curr = root
            while curr:
                curr = curr.right
                height += 1
            return height

        def count_nodes(root):
            if not root: 
                return 0
            left_height = FindLeftHeight(root)
            right_height = FindRightHeight(root)
            print(left_height, right_height)
            if left_height == right_height:
                return (2**left_height) - 1
            else:
                return 1 + count_nodes(root.left) + count_nodes(root.right)
        
        return count_nodes(root)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna