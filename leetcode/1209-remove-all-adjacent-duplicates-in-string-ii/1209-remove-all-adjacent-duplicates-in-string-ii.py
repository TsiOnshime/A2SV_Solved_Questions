class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]

        for i in range(1, len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])
        
        ans = []
        for i in range(len(stack)):
            ans.append(stack[i][0] * stack[i][1])

        return "".join(ans)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna