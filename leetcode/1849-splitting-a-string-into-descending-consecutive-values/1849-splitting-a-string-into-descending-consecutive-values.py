class Solution:
    def splitString(self, s: str) -> bool:
        
        def is_valid_state(start):
            return start == len(s)

        def search(start, prev):
            if is_valid_state(start):
                return True

            for j in range(start, len(s)):
                val = int(s[start:j + 1])

                if prev == val + 1 and search(j + 1, val):
                    return True
            return False

        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if search(i + 1, val):
                return True
        return False