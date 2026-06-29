class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x:x[1])
        dp = [[0] * (len(pairs) + 1) for _ in range(len(pairs))]

        max_length = 0
        def findlength(i, prev):
            nonlocal dp
            if i == len(pairs):
                return 0
            if dp[i][prev + 1]:
                return dp[i][prev + 1]


            # take 
            take = 0
            if prev == -1 or pairs[prev][1] < pairs[i][0]:
                take = 1 + findlength(i + 1, i)
            # no take
            notake = findlength(i + 1, prev)

            dp[i][prev + 1] = max(take, notake)
            return dp[i][prev + 1]
        

        for i in range(len(pairs)):
            max_length = max(max_length, findlength(i, -1))
        
        return max_length
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna