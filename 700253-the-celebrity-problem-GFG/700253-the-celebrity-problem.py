class Solution:
    def celebrity(self, mat):
        # code here
        rows, cols = len(mat), len(mat[0])
        known = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                known[j] += mat[i][j]
        count, ind = 0, -1
        for i in range(cols):
            if known[i] == cols:
                count += 1
                ind =i
        if count != 1:
            return -1
        for i in range(cols):
            if ind != i and mat[ind][i] != 0:
                return -1
        return ind

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna