class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')': '(', '}': '{', ']': '['}

        for i in range(len(s)):
            if s[i] in parenthesis:
                if stack and stack[-1] == parenthesis[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        if stack:
            return False
        return True