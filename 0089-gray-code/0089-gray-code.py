class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]

        for i in range(n):
            for num in reversed(res):
                res.append(num + (1 << i))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna