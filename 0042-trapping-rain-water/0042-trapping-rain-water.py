class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL, maxR = height[l], height[r]

        rain = 0
        while l <= r:
            if maxL <= maxR:
                diff = maxL - height[l]
                if diff > 0:
                    rain += diff
                l += 1
                maxL = max(maxL, height[l - 1])

            else:
                diff = maxR - height[r]
                if diff > 0:
                    rain += diff
                r -= 1
                maxR = max(maxR, height[r + 1])

        return rain





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna