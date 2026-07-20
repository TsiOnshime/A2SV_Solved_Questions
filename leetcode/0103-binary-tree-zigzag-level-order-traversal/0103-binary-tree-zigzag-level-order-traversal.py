# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()

        queue.append(root)
        temp = []
        right = True
        res = [[root.val]]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if right:
                    for neigh in [node.left, node.right]:
                        if neigh:
                            temp.append(neigh)
                else:
                    for neigh in [node.right, node.left]:
                        if neigh:
                            temp.append(neigh)
            right = not right
            if temp:
                res.append([])
            for i in range(len(temp) - 1, -1, -1):
                res[-1].append(temp[i].val)             
            while temp:
                queue.append(temp.pop())
                
        return res
                    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna