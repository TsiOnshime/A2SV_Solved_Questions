class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in {"+", "/", "-", "*"}:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
        
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(tokens[i])
        
        return int(stack[0])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna