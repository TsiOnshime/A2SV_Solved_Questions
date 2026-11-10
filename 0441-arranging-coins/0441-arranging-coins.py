class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        ans = 0
        while l <= r:
            mid = l + (r - l)//2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                ans = max(mid, ans)
                l = mid + 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna