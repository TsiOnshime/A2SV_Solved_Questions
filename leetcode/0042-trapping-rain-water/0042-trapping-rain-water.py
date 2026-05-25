class Solution:
    def trap(self, height: List[int]) -> int:
        maxRight = [0] * len(height)
        maxLeft = [0] * len(height)

        rain = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                rain += diff

        return rain


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna