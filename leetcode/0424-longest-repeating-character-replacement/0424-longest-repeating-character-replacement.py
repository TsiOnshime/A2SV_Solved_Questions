class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        maxFreq = 0
        max_length = 0
        l, r = 0, 0
        chars = [0] * 26
        offset = ord('A')

        while r < len(s):
            chars[ord(s[r]) - offset] += 1
            maxFreq = max(maxFreq, chars[ord(s[r]) - offset])
            length += 1
            if length - maxFreq > k:
                chars[ord(s[l]) - offset] -= 1
                l += 1
                length -= 1
            if length - maxFreq <= k:
                max_length = max(max_length, length)
            r += 1
        return max_length


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna