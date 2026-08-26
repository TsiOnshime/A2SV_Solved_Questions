class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        i = 0
        j = 0

        n = len(v1)
        m = len(v2)

        while i < n or j < m:
            n1 = v1[i] if i < n else 0
            n2 = v2[j] if j < m else 0

            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
            i += 1
            j += 1
        return 0

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna