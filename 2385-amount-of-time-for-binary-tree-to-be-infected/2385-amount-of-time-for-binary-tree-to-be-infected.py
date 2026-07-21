# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.val == start:
                start = node
            for neigh in [node.left, node.right]:
                if neigh:
                    parent[neigh] = node
                    queue.append(neigh)
   
        max_time = 0
        queue = deque()
        visited = set()
        queue.append([start, 0])
        visited.add(start)

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for neigh in [node.left, node.right]:
                if neigh and neigh not in visited:
                    visited.add(neigh)
                    queue.append([neigh, time + 1])
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                queue.append([parent[node], time + 1])
        
        return max_time



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna