class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = defaultdict(int)
        
        for i in range(len(t)):
            chars[t[i]] += 1
        
        l, r = 0, 0
        matched = 0
        res = [-1, float('inf')]
        while r < len(s):
            if chars[s[r]] > 0:
                matched += 1
            chars[s[r]] -= 1
            while matched == len(t):
                if r - l + 1 < res[1]:
                    res = [l, r - l + 1]
                chars[s[l]] += 1
                if chars[s[l]] > 0:
                    matched -= 1
                l += 1
            r += 1
        return s[res[0]:res[0] + res[1]] if res[0] != -1 else ""


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna