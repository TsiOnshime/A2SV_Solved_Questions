class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                matches, nomatches = float('-inf'), float('-inf')
                if text1[i - 1] == text2[j - 1]:
                    matches = 1 + prev[j - 1]
                else:
                    nomatches = 0 + max(prev[j], curr[j - 1])
                val = max(matches, nomatches)
                curr[j] = val      
            prev = curr.copy()

        return prev[m]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna