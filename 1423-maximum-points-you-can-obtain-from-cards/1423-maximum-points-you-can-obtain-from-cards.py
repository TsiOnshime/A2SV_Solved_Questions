class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        max_sum = 0

        for i in range(k):
            lsum += cardPoints[i]
        max_sum = max(max_sum, lsum)

        r = len(cardPoints) - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[r]
            r -= 1
            max_sum = max(max_sum, lsum + rsum)
        
        return max_sum
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna