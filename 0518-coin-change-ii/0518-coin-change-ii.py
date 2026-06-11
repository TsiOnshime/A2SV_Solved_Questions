class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        prev = [0] * (amount + 1)
        curr = [0] * (amount + 1)
        for i in range(amount + 1):
            prev[i] = 1 if i % coins[0] == 0 else 0

        for i in range(1, len(coins)):
            for target in range(amount + 1):
                notake = prev[target]
                take = 0
                if coins[i] <= target:
                    take = curr[target - coins[i]]
                val = notake + take
                curr[target] = val
            prev = curr.copy()
        return prev[amount]




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna