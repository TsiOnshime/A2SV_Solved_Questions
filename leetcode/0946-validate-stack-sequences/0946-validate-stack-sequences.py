class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while i < len(pushed) and j < len(popped):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1

        while j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna