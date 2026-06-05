class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows, cols = len(triangle), len(triangle[-1])
        
        dp = [[-1] * cols for i in range(rows)]

        for i in range(rows):
            cols = i + 1
            j = 0
            while j < cols:
                if i == 0 and j == 0:
                    dp[i][j] = triangle[i][j]
                else:
                    up = float('inf')
                    upleft = float('inf')

                    if i - 1 >= 0 and j < prevCol:
                        up = dp[i - 1][j]
                    if j - 1 >= 0:
                        upleft = dp[i - 1][j - 1]
                    val = min(up, upleft)
                    dp[i][j] = val + triangle[i][j]
                
                j += 1
            prevCol = cols
        return min(dp[-1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna