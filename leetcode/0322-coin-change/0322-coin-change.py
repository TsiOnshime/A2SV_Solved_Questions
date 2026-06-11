class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        prev = [float('inf')] * (amount + 1)
        curr = [float('inf')] * (amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
        
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                notake = 0 + prev[j]
                take = float('inf')
                if coins[i] <= j:
                    take = 1 + curr[j - coins[i]]
                curr[j] = min(notake, take)
            prev = curr.copy()

        res = prev[amount]
        return res if res != float('inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna