class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s2 = {}
        count_s1 = {}
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
        
        if count_s1 == count_s2:
            return True
        l, r = 0, len(s1)
        while r < len(s2):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]

            if count_s1 == count_s2:
                return True
            l += 1
            r += 1
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna