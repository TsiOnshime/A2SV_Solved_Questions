class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_length = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna