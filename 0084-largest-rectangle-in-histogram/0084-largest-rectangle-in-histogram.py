class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # it is all about finding the pse and nse 
        stack = []
        max_area = 0
        # [2]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                pse = stack[-1] if stack else -1
                nse = i
                area = heights[idx] * (nse - pse - 1)
                max_area = max(max_area, area)

            stack.append(i)
        
        nse = len(heights)
        while stack:
            idx = stack.pop()
            pse = stack[-1] if stack else -1
            area = heights[idx] * (nse - pse - 1)
            max_area = max(max_area, area)

        return max_area


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna