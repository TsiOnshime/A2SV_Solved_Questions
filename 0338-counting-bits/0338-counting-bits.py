class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i & 1
                i = i >> 1
            ans.append(count)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna