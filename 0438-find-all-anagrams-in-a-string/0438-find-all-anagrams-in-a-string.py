class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        chars_s = {}
        chars_p = {}
        res = []

        for i in range(len(p)):
            chars_p[p[i]] = chars_p.get(p[i], 0) + 1
            chars_s[s[i]] = chars_s.get(s[i], 0) + 1  
        if chars_p == chars_s:
            res.append(0)
        l, r= 0, len(p)
        while r < len(s):
            chars_s[s[r]] = chars_s.get(s[r], 0) + 1
            chars_s[s[l]] -= 1
            if chars_s[s[l]] == 0:
                del chars_s[s[l]]
            l += 1
            if chars_s == chars_p:
                res.append(l)
            r += 1
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna