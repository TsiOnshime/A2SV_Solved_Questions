class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # next minimum element
        # we iterate from the back 
        # if our stack is empty we keep the element as is
        # if the top element of our stack is lesser at that elements index we update the value to prices[i] - stack[-1] and append the price at the stack
        # else if the top element of our stack is greater than prices[i]:
        # we pop the top of our stack until it is lesser or our stack is empty

        answer = prices[:]
        stack = []
        for i in range(len(prices) - 1, -1 , -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack and stack[-1] <= prices[i]:
                answer[i] -= stack[-1]
            stack.append(prices[i])

        
        return answer
            
