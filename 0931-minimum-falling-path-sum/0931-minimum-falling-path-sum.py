class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev = [float('inf')]*cols
        curr = [0] * cols

        for i in range(cols):
            prev[i] = matrix[rows - 1][i]


        for i in range(rows - 2, -1, -1):
            for j in range(cols):
      
                down = prev[j]
                downleft = float('inf')
                downright = float('inf')

                if j - 1 >= 0:
                    downleft = prev[j - 1]
                if j + 1 < cols:
                    downright = prev[j + 1]

                val = min(down, downleft, downright)
                curr[j] = val + matrix[i][j]
            prev = curr.copy()

        return min(prev)

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna