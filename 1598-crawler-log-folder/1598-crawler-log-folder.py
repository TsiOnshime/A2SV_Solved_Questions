class Solution:
    def minOperations(self, logs) :
        # "../" move to parent 
        # "./" remain there
        # "x" move to chile dolder

        stack = []
        

        for i in logs:
            if i == "../":
                if stack:
                    stack.pop()
                else:
                    continue
            elif i == "./":
                continue
            else:
                stack.append(i)
        return len(stack)
