class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            while stack and stack[-1] == char:
                stack.pop()
                if not stack or stack[-1] != char:
                    break
            else:
                stack.append(char)
        
        return "".join(stack)
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna