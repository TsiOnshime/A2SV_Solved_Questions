class Solution:
    def splitString(self, s: str) -> bool:
        

        def is_valid_state(start):
            if start == len(s):
                return True

        def search(start, prev):
            if is_valid_state(start):
                return True
            
            for j in range(start, len(s)):
                val = int(s[start:j + 1])
                if val + 1 == prev and search(j + 1, val):
                    return True
                if val + 1 > prev:
                    return
            return False






        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if search(i + 1, val):
                 return True
        
        return False