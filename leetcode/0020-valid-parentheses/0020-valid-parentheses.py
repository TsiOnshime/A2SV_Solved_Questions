class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == parenthesis[i]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False