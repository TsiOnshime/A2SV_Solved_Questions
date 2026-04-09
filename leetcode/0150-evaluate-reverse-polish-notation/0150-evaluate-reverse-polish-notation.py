import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}
       
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if tokens[i] == "+":
                    result = op1 + op2
                elif tokens[i] == "-":
                    result = op2 - op1
                elif tokens[i] == "*":
                    result = op2 * op1
                else:
                    result = int(op2 / op1)
                stack.append(result)
            
            else:
                stack.append(tokens[i])
        
        return int(stack[0])