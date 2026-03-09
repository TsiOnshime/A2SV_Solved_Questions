class Solution:
    def maxScore(self, s: str) -> int:
        # p = [0, 1, 2, 3, 3, 3, 4]
            
        # i == p[i]
        # right 
        _sum = 0
        for i in range(len(s)):
            _sum += int(s[i])
        
        left = 0
        right = _sum
        score = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            score = max(score , left + right)
        return score


