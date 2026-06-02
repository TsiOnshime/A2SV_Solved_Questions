class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()

        for i in range(n):
            queue.append(i)

        while len(queue) > 1:
            for i in range(k - 1):
                val = queue.popleft()
                queue.append(val)
            queue.popleft()
        return queue[0] + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna