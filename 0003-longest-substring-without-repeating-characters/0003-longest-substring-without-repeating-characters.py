class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        count = defaultdict(int)

        l = 0
        r = 0
        while r < len(s):
            count[s[r]] += 1
            while count[s[r]] > 1:

                count[s[l]] -= 1
                l += 1
            print(l)
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna