class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        result.append([1])

        for i in range(1, numRows):
            row = []
            prev = result[-1]
            for j in range(i + 1):
                elem1 = prev[j] if j < len(prev) else 0
                elem2 = prev[j - 1] if j - 1 >= 0 else 0

                row.append(elem1 + elem2)
            result.append(row)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna