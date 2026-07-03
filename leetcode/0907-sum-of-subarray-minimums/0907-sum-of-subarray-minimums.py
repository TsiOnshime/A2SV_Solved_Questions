class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def findNse():
            nse = [len(arr)] * len(arr)
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                nse[i] = stack[-1] if stack else len(arr)
                stack.append(i)
            return nse
        
        def findPse():
            pse = [-1] * len(arr)
            stack = []
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()

                pse[i] = stack[-1] if stack else -1
                stack.append(i)
            return pse


        MOD = 10**9 + 7
        _sum = 0
        pse = findPse()
        nse = findNse()
        for i in range(len(arr)):
            leftBoundary = pse[i]
            rightBoundary = nse[i]

            ways = (i - leftBoundary) * (rightBoundary - i) 

            _sum = (_sum + ways * arr[i]) % MOD

        return _sum




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna