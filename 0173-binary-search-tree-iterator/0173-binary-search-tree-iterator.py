# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def traverse(self, root):
        if not root:
            return 

        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)




    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.traverse(root)
        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer]

    def hasNext(self) -> bool:
        if self.pointer + 1 < len(self.inorder):
            return True
        return False
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna