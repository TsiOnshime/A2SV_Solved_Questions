class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        l = len(s3)
        cache = {}
        if n + m != l:
            return False

        def check(i, j):

            if i == n and j == m:
                return True
            if (i, j) in cache:
                return cache[(i, j)]

            result = False
            k = i + j
            if i < n and s1[i] == s3[k]:
                result =  check(i + 1, j)
                        
            if not result and j < m and s2[j] == s3[k]:
                result = check(i, j + 1)
                        
            cache[(i, j)] = result
            return result
        return check(0, 0)
             




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna