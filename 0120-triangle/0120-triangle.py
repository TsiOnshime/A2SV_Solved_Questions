class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        def pathSum(i, j):
            if i == rows - 1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i, j)]
            down = triangle[i][j] + pathSum(i + 1, j)
            diagonal = triangle[i][j] + pathSum(i + 1, j + 1)

            val = min(down, diagonal)
            memo[(i,j)] = val
            return val
        

        memo = {}
        return pathSum(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna