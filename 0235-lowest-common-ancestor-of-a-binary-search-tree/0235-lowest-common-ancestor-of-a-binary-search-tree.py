# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.val == p.val or node.val == q.val:
                return node
            elif p.val < node.val < q.val or q.val < node.val < p.val:
                return node

            for neigh in [node.left, node.right]:
                if neigh:
                    queue.append(neigh)

