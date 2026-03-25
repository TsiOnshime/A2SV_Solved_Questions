class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        arr = list(s)
        print(arr)
    
        for i in range(len(s)):
            
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    arr[i] = ""
            if s[i] == "(":
                stack.append(i)
        print(stack)
        for i in stack:
            arr[i] = ""
        
        return "".join(arr)