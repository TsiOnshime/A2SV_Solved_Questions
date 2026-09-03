class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [1]

        for i in range(1, rowIndex + 1):
            row = []
            for j in range(i + 1):
                elem1 = prev[j] if j < len(prev) else 0
                elem2 = prev[j - 1] if j - 1 >= 0 else 0

                row.append(elem1 + elem2)
            
            prev = row
        
        return prev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna