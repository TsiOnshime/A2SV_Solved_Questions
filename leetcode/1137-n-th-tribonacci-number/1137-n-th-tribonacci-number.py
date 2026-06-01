class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:return 0
        if n == 1:return 1
        if n == 2:return 1
        values = [0] * (n + 1)
        values[1] = 1
        values[2] = 1

        for i in range(3, n + 1):
            values[i] = values[i - 3] + values[i - 2] + values[i - 1]

        return values[n]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna