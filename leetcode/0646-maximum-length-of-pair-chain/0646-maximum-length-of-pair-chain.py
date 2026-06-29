class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev = pairs[0][1]
        length = 1

        for i in range(1, len(pairs)):
            if prev < pairs[i][0]:
                length += 1
                prev = pairs[i][1]
        
        return length


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna