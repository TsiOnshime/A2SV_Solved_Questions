class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_be_removed = set()
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    to_be_removed.add(i)
        while stack:
            to_be_removed.add(stack.pop())

        res = []
        for i in range(len(s)):
            if i in to_be_removed:
                continue
            res.append(s[i])
        
        return "".join(res)
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna