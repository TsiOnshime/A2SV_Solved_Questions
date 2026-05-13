class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna