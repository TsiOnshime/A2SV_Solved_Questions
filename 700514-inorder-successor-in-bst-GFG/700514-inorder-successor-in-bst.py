'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrderSuccessor(self, root, k):

        curr = root
        ans = -1
        while curr:
            if curr.data <= k.data:
                curr = curr.right
            else:
                ans = curr.data
                curr = curr.left
        return ans
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna