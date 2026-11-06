class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split(" ")
        res = []
        for j in range(len(new_s) - 1, -1, -1):
            if len(new_s[j]) == 0:
                continue
            res.append(new_s[j])
        
        return " ".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna