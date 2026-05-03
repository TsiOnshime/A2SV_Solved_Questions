class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currentCost = 0
        l = 0
        maxLength = 0
        for r in range(len(s)):
            currentCost += abs(ord(s[r]) - ord(t[r]))
            while currentCost > maxCost:
                currentCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            maxLength = max(maxLength, r - l + 1)

        return maxLength