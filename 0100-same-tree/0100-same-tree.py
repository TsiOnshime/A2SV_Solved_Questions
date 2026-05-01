# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()
        queue1.append(p)
        queue2.append(q)
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and not node2: 
                return False
            elif not node1 and node2:
                return False
            elif not node1 and not node2:
                continue
            elif node1.val != node2.val:
                return False
            if node1:
                for neigh in [node1.left, node1.right]:
                    queue1.append(neigh)
            if node2:
                for neigh in [node2.left, node2.right]:
                    queue2.append(neigh)
        
        return len(queue1) == len(queue2)
