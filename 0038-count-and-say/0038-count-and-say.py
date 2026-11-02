class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = []
        count = 1

        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                result.append(f"{str(count)}{prev[i]}")
                count = 1
        return "".join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna