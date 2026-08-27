class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        # idx, count_max
        res = [-1, -1]
        def count_ones(row):
            ones = 0
            for i in range(cols):
                if mat[row][i] == 1:
                    ones += 1
            return ones
        for r in range(rows):
            idx, count_max = res
            cnt = count_ones(r)
            if cnt > count_max:
                res = [r, cnt]

        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna