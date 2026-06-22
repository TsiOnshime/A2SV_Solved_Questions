class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        n, m = len(matrix), len(matrix[0])

        def findMaximumArea(arr):
            stack = []  # (height, start_index)
            max_area = 0

            for i in range(m):
                start = i

                while stack and stack[-1][0] > arr[i]:
                    height, idx = stack.pop()
                    max_area = max(max_area, height * (i - idx))
                    start = idx

                stack.append((arr[i], start))

            # Remaining bars extend to the end
            while stack:
                height, idx = stack.pop()
                max_area = max(max_area, height * (m - idx))

            return max_area

        heights = [0] * m
        max_area = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else: heights[j] = 0

            max_area = max(max_area, findMaximumArea(heights))

        return max_area


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna