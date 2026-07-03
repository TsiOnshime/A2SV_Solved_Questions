class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                rain += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                rain += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])

        return rain


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna