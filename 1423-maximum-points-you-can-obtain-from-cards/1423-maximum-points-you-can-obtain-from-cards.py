class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # a subarray which has length of len(cardPoints) - k and has minimum sum

        l = 0
        r = 0
        length = len(cardPoints) - k
        ans = float('inf')
        _sum = 0
        for i in range(length):
            _sum += cardPoints[i]
        r = length 
        ans = min(ans, _sum)

        while r < len(cardPoints):
            _sum += cardPoints[r]
            while r - l + 1 > length:
                _sum -= cardPoints[l]
                l += 1
            ans = min(ans, _sum)
            r += 1
        return sum(cardPoints) - ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna