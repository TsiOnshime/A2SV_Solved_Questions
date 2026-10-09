class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        l = len(s3)
        cache = {}
        if n + m != l:
            return False

        def check(i, j, k):

            if i == n and j == m and k == l:
                return True
            if (i, j, k) in cache:
                return cache[(i, j, k)]
            
            if i < n and k < l:
                if s1[i] == s3[k]:
                    if check(i + 1, j, k + 1):
                        cache[(i, j, k)] = True
                        return True
            if j < m and k < l:
                if s2[j] == s3[k]:
                    if check(i, j + 1, k + 1):
                        cache[(i, j, k)] = True
                        return True
            cache[(i, j, k)] = False
            return False
        return check(0, 0, 0)
             




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna