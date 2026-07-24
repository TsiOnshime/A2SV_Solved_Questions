'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def LCA(self, root, n1, n2):
      
        curr = root
        ancestor = root
        while curr:
            ancestor = curr
            if curr.data > n1.data and curr.data < n2.data:
                break
            elif curr.data < n1.data and curr.data > n2.data:
                break
            elif curr.data == n1.data:
                break
            elif curr.data == n2.data:
                break
            elif curr.data < n1.data and curr.data < n2.data:
                curr = curr.right
            elif curr.data > n1.data and curr.data > n2.data:
                curr = curr.left
        return ancestor
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna