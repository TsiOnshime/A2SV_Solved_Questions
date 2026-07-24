# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root

        curr = self.root
        self.stack.append(curr)
        while curr.left:
            curr = curr.left
            self.stack.append(curr)
        



    def next(self) -> int:
        if not self.stack:
            return 
        elem = self.stack[-1]
        curr = self.stack.pop()
        if curr.right:
            curr = curr.right
            self.stack.append(curr)
            while curr.left:
                curr = curr.left
                self.stack.append(curr)
        
        return elem.val
        

    def hasNext(self) -> bool:
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna