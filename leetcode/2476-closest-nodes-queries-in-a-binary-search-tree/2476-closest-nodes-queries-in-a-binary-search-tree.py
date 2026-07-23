# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        

        
        inorder = []

        curr = root
        while curr:
            if curr.left == None:
                inorder.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right == None:
                    temp.right = curr
                    curr = curr.left
                else:
                    inorder.append(curr.val)
                    temp.right = None
                    curr = curr.right
        
        def binarySearch(inorder, val):
            _min = -1
            _max = -1

            l, r = 0, len(inorder) - 1

            while l <= r:
                mid = l + (r - l)//2
                if inorder[mid] == val:
                    return [val, val]
                elif inorder[mid] > val:
                    _max = inorder[mid]
                    r = mid - 1
                else:
                    _min = inorder[mid]
                    l = mid + 1
            return [_min, _max]
        ans = []
        for val in queries:
            ans.append(binarySearch(inorder, val))
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna