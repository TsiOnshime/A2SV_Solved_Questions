class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        count = 0
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def countChange(i, target):
            nonlocal count
            if i == 0:
                return 1 if target % coins[0] == 0 else 0
            if dp[i][target] != -1:
                return dp[i][target]

            notake = countChange(i - 1, target)
            take = 0
            if coins[i] <= target:
                take = countChange(i, target - coins[i])

            val = take + notake
            dp[i][target] = val
            return val
        
        return countChange(len(coins) - 1, amount)
        

        return count 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna