class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna