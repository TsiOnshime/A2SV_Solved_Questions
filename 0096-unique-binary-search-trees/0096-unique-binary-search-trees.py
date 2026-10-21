class Solution:
    def numTrees(self, n: int) -> int:
        ways = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                right = root - 1
                left = nodes - root 
                total += ways[left] * ways[right]
            ways[nodes] = total 
            
        return ways[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna