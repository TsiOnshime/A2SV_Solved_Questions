class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = set()
        provinces = 0

        def bfs(start):
            queue = deque([start])
            visited.add(start)

            while queue:
                curr = queue.popleft()
                for i in range(n):

                    if i not in visited and isConnected[curr][i]== 1:
                        queue.append(i)
                        visited.add(i)

        for i in range(n):
            if i not in visited:
                bfs(i)
                provinces += 1

        return provinces


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna