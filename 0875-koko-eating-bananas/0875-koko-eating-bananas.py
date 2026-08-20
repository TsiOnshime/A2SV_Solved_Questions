class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        ans = sum(piles)
# [3,6,7,11], h = 8
# l = 1,   r = 27
# mid = 14
        def is_valid(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            return time <= h

                        
        while l <= r:
            mid = l + (r - l)//2
            if is_valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna