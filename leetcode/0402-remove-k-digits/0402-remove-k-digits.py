class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        res = []
        while stack:
            res.append(stack.pop())
        
        while res and res[-1] == "0":
            res.pop()

        res = list(reversed(res))
        if len(res) == 0:
            return "0"
        return "".join(res)

  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna