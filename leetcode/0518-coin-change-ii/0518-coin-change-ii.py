class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(amount + 1):
            dp[0][i] = 1 if i % coins[0] == 0 else 0

        for i in range(1, len(coins)):
            for target in range(amount + 1):
                notake = dp[i - 1][target]
                take = 0
                if coins[i] <= target:
                    take = dp[i][target - coins[i]]
                val = notake + take
                dp[i][target] = val
        return dp[len(coins) - 1][amount]




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna