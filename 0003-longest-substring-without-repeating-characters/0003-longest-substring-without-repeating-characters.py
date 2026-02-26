class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = float('-inf')
        length = 0

        l = 0
        r = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        while r < len(s):
            s_counter = Counter(s[l:r+1])

            if s_counter[s[r]] > 1:
                l += 1
            else: 
                length = len(s[l:r+1])
                r += 1

            longest = max(longest, length)
        return longest
            

