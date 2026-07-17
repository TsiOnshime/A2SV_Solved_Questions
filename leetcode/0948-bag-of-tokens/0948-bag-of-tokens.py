class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
              
            else:
                if score >= 1:
                    power += tokens[r]
                    score -= 1
                    r -= 1
                else:
                    break
            max_score = max(max_score, score)
        return max_score


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna