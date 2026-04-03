class Solution:
    def smallestNumber(self,pattern):
        ## But still try to come up with a backtracking solution that doesn't time exceed
        ### Stack is powerful ###

        ##wow##
        stack = []
        output = []
        j = 0

        while j < len(pattern) + 1:
            stack.append(str(j + 1))

            if j == len(pattern):
                break
            if pattern[j] == "I":
                while stack:
                    output.append(stack.pop())

            j += 1

        while stack:
            output.append(stack.pop())

        return "".join(output)