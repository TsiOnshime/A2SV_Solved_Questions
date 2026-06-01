class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        ways = [1, 2]
        curr = 3
        i = 2
        while curr != n:
            way = ways[i - 1] + ways[i - 2]
            ways.append(way)
            i += 1
            curr += 1

        return ways[-1] + ways[-2]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna