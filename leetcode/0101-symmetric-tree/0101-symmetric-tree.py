# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (root.left and not root.right) or (not root.left and root.right):
            return False
        if not root.left and not root.right:
            return True

        queue1 = deque()
        queue2 = deque()
# q1 = [3, 4] n1 = 2
# q2 = [3, 4] n2 = 2
        queue1.append(root.left)
        queue2.append(root.right)

        temp1 = [root.left.val]
        temp2 = [root.right.val]

        while queue1 and queue2:
            if temp1 != temp2:
                return False
            temp1 = []
            temp2 = []
            n = len(queue1)
            for i in range(n):
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if node1:
                    for neigh in [node1.left, node1.right]:
                        if not neigh:
                            temp1.append(None)
                        else:
                            temp1.append(neigh.val)
                        queue1.append(neigh)
                if node2:
                    for neigh in [node2.right, node2.left]:
                        if not neigh:
                            temp2.append(None)
                        else:
                            temp2.append(neigh.val)
                        queue2.append(neigh)
        return True
                
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna