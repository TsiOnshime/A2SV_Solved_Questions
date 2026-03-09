class Solution:
    def maxScore(self, s: str) -> int:
        # p = [0, 1, 2, 3, 3, 3, 4]
            
        # i == p[i]
        # right 
        s_list = [0] * len(s)
        for i in range(len(s)):
            s_list[i] = int(s[i])
        for i in range(1, len(s)):
            s_list[i] += s_list[i - 1]
        print(s_list)
        left = 0
        right = s_list[-1]
        score = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            score = max(score , left + right)
        return score


