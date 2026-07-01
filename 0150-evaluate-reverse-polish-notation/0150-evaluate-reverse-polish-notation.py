class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        ops = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                operands.append(tokens[i])
            else:
                
                second = int(operands.pop())
                first = int(operands.pop())
                if tokens[i] == "+": res = first + second
                elif tokens[i] == "-": res = first - second
                elif tokens[i] == "*": res = first * second
                else: res = int(first / second)
                operands.append(res)
        return int(operands[0])



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna