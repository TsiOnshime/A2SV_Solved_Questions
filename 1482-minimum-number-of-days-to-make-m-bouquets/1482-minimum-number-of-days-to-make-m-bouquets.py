class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        flowers_needed = m * k
        ans = -1
        if flowers_needed > len(bloomDay):
            return -1
        
        def is_valid(mid):
            flowers = 0
            bouque = 0
            for i in range(len(bloomDay)):
                if mid >= bloomDay[i]:
                    flowers += 1
                    if flowers == k:
                        bouque += 1
                        flowers = 0
                else:
                    flowers = 0
                    
                
            return bouque >= m

        l, h = 1, max(bloomDay)

        while l <= h:
            mid = l + (h - l)//2
            if is_valid(mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna