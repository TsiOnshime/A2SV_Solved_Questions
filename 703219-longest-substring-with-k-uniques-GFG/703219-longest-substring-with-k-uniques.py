class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l, r = 0, 0
        length = -1
        chars = {}
        
        while r < len(s):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1
            
            while len(chars) > k:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            if len(chars) == k:
                length = max(length, r - l + 1)
            r += 1
        return length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna