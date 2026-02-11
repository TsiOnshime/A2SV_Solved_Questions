class Solution:
    def findValidPair(self, s: str) -> str:

        s_counter = Counter(s)
        print(s_counter)
        for i in range(len(s)-1):
            
            if s[i] != s[i + 1] and s_counter[s[i]] == int(s[i]) and s_counter[s[i+1]]== int(s[i+1]):
                return s[i:i+2]
        return ""