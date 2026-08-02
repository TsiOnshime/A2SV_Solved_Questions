class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        # l = 1, r = 8
        # area = 0,     width = 8, hgt = 1
        while l <= r:
            width = r - l 
            hgt = min(height[l], height[r])
            area = max(width * hgt, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna