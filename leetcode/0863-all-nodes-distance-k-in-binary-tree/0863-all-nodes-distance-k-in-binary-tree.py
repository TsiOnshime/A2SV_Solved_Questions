# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(TreeNode)
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            for neigh in [node.left, node.right]:
                if neigh:
                    parent[neigh] = node
                    queue.append(neigh)
        
        queue = deque()
        visited = set()
        res = []

        queue.append([target, 0])
        visited.add(target)

        while queue:
            node, dist = queue.popleft()
            if dist == k: res.append(node.val)
            for neigh in [node.left, node.right]:
                if neigh and neigh not in visited:
                    queue.append([neigh, dist + 1])
                    visited.add(neigh)
                if node in parent:
                    if parent[node] not in visited:
                        queue.append([parent[node], dist + 1])
                        visited.add(parent[node])

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna