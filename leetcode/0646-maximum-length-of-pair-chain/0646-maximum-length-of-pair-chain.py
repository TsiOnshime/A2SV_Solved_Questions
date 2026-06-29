class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x:x[1])
        dp = [0] * len(pairs)
        max_length = 0
        def findlength(i, prev):
            nonlocal dp
            if i == len(pairs):
                return 0
            if dp[i]:
                return dp[i]

            # take 
            take = 0
            if prev < pairs[i][0]:
                take = 1 + findlength(i + 1, pairs[i][1])
            # no take
            notake = findlength(i + 1, prev)

            dp[i] = max(take, notake)
            return dp[i]
        

        for i in range(len(pairs)):
            max_length = max(max_length, findlength(i, float('-inf')))
        
        return max_length
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna