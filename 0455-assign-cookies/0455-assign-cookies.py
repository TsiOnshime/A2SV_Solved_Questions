class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        j = len(s) - 1
  
        for i in range(len(g) - 1, -1, -1):
            if j < 0:
                break
            if g[i] <= s[j]:
                content += 1
                j -= 1

        return content


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna