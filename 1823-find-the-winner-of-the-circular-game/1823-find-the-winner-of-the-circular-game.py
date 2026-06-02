class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0

        for people in range(1, n + 1):
            res = (res + k) % people

        return res + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna