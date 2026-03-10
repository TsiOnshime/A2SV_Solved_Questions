class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # target = [2,3]
        #           i
        # stack = []
        # list = [1,2,3]
        # output = ["push","push","pop","push"]
        # stack = [1,3]
        #          j
        

        # target = [1,2,3]
        #               i
        # stack = []
        # list = [1,2,3]
        # output = ["push","push","push"]
        # stack = [1,2,3]
        #              j

        # initialize an empty stack = [], two pointers i = for pointing at target and j for pointing at stack both initialized to be 0
        # iterate through 1 to n + 1
        # push 1 to the stack
        # output.append("push")
        # compare stack[j] and target[i]:
            #if  equal  increment both i and j by 1
            #else pop stack
            # stack == target : return output
        stack = []
        output = []
        i = 0
        j = 0
        for num in range(1, n + 1):
            if stack == target:
                return output
            stack.append(num)
            output.append("Push")
            if stack[j] == target[i]:
                i += 1
                j += 1
            else:
                stack.pop()
                output.append("Pop")
        return output