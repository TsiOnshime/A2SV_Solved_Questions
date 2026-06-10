class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = {}
        def longestChain(i,prevIndex):
            if i == len(pairs):
                return 0
            if (i, prevIndex) in dp:
                return dp[(i, prevIndex)]

            notake = longestChain(i + 1, prevIndex)
            take = 0
            if prevIndex == -1 or pairs[i][0] > pairs[prevIndex][1]:
                take = 1 + longestChain(i + 1, i)

            val = max(notake, take)
            dp[(i, prevIndex)] = val
            return val

        return longestChain(0, -1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna