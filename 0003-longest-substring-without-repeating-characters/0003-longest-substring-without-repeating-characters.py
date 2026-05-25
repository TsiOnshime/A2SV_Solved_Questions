class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_freq = defaultdict(int)
        length = 0
        l = 0
        # r = 3 l = 1
        # abcabcbb
        # {a: 1, b: 1, c: 1}
        for r in range(len(s)):
            char_freq[s[r]] += 1
            while char_freq[s[r]] > 1:
                char_freq[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)

        return length



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna