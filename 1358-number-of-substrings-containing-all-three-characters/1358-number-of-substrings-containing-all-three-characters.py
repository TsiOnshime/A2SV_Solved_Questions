class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        chars = [-1] * 3
        offset = ord('a')
        count = 0
        for i in range(len(s)):
            chars[ord(s[i]) - offset] = i
            if min(chars) != -1:
                count += (1 + min(chars))
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna