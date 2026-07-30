class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] == 0:
                    continue
                else:
                    right = mat[r][c + 1] if c + 1 < cols else float('inf')
                    down = mat[r + 1][c] if r + 1 < rows else float('inf')

                    mat[r][c] = min(right + 1, down + 1)

        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue
                else:
                    left = mat[r][c - 1] if c - 1 >= 0 else float('inf')
                    up = mat[r - 1][c] if r - 1 >= 0 else float('inf')

                    mat[r][c] = min(left + 1, up + 1, mat[r][c])

        return mat

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna