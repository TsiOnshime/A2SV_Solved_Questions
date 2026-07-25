# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BinarySearchTreeIterator:
    def __init__(self, root: Optional[TreeNode], reverse):
        self.root = root
        self.stack = [self.root]
        self.reverse = reverse

        if not self.reverse:
            curr = self.root.left
            self.pushAll(curr, self.reverse)

        else:
            curr = self.root.right
            self.pushAll(curr, self.reverse)


            
    def next(self):
        if not self.stack:
            return
        curr = self.stack.pop()
        elem = curr.val
        if not self.reverse:
            if curr.right:
                curr = curr.right
                self.pushAll(curr, self.reverse)
        else:
            if curr.left:
                curr = curr.left
                self.pushAll(curr, self.reverse)
            
        return elem

    def pushAll(self, curr, reverse):
        while curr:
            self.stack.append(curr)
            curr = curr.left if not reverse else curr.right
    
    def hasNext(self):
        return len(self.stack) > 0
                


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = BinarySearchTreeIterator(root, False)
        r = BinarySearchTreeIterator(root, True)
        
        i = l.next()
        j = r.next()
        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = l.next()
            else:
                j = r.next()

        return False







# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna