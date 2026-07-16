class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r= 0, 0
        chars_s = {}
        chars_p = {}
        res = []
        for char in p:
            chars_p[char] = chars_p.get(char, 0) + 1
     
        
        while r < len(s):
            if s[r] not in chars_p:
                r += 1
                l = r 
                chars_s = {}
                continue
            chars_s[s[r]] = chars_s.get(s[r], 0) + 1
            while chars_s[s[r]] > chars_p[s[r]]:
                chars_s[s[l]] -= 1
                l += 1
            if chars_s == chars_p:
                res.append(l)
            r += 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna