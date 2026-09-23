class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        count = 0
        num = 0
        i = 0
        coins.sort()
        while num < target:
            if i < len(coins) and coins[i] <= num + 1:
                num += coins[i]
                i += 1
            else:
                count += 1
                num += (num + 1)

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna