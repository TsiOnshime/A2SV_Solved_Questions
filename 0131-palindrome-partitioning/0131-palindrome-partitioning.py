class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        # i => start of the new partition
        # j => 
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def partS(i):
            nonlocal res
            nonlocal path
            if i == len(s):
                res.append(path.copy())
                return

            for k in range(i, len(s)):
                if isPalindrome(i, k):
                    path.append(s[i: k + 1])
                    partS(k + 1)
                    path.pop()
                
        partS(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna