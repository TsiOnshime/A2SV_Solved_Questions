class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete = 0
        coins_left = n
        stair = 1
        while coins_left > 0:
            if coins_left - stair >= 0:
                coins_left -= stair
                complete += 1
            else:
                break
            stair += 1
        return complete
    




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna