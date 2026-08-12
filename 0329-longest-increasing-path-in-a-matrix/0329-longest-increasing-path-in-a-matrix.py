class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_length = float('-inf')
        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c, prev):
            nonlocal max_length
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if prev >= matrix[r][c]:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            
            left = dfs(r, c - 1, matrix[r][c])
            right = dfs(r, c + 1, matrix[r][c])
            up = dfs(r - 1, c, matrix[r][c])
            down = dfs(r + 1, c, matrix[r][c])

            length = max(left, right, up, down) + 1
            memo[(r, c)] = length

            max_length = max(max_length, length)

            return length
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in memo:
                    dfs(r, c, float('-inf'))
        

        return max_length




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna