import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack = []

        for op in tokens:
            if op in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                
                expression = int(eval(str(op2) + op + str(op1)))
                        
                stack.append(expression)
                continue
            stack.append(op)
                    
        return int(stack[0])