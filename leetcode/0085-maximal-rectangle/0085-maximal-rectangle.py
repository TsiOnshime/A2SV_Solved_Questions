class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        
        heights = [0] * cols

        def findMaxArea(heights):
        # [3, 1, 2, 3, 2]
        # stack = [1, 2, 4] p = 2, n = 4, area = 3 
            stack = []
            area = 0
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    pse = stack[-1] if stack else -1
                    nse = i
                    area = max(area, heights[idx] * (nse - pse - 1))
                stack.append(i)

            nse = len(heights)
            while stack:
                idx = stack.pop()
                pse = stack[-1] if stack else -1
                area = max(area, heights[idx] * (nse - pse - 1))
    
            return area



        for i in range(rows-1, -1, -1):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, findMaxArea(heights))

        return max_area





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna