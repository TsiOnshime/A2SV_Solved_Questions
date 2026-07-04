class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        def findPSEE():
            psee = [-1] * len(nums)
            stack = []
            for i in range(len(nums)):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                psee[i] = stack[-1] if stack else -1
                stack.append(i)
            return psee

        def findNSE():
            nse = [len(nums)] * len(nums)
            stack = []
            for i in range(len(nums) - 1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                nse[i] = stack[-1] if stack else len(nums)
                stack.append(i)
            return nse

        def findPGEE():
            pge = [-1] * len(nums)
            stack = []

            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                pge[i] = stack[-1] if stack else -1
                stack.append(i)
            return pge
        
        def findNGE():
            nge = [len(nums)] * len(nums)
            stack = []

            for i in range(len(nums) - 1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                nge[i] = stack[-1] if stack else len(nums)
                stack.append(i)
            return nge

        pgee = findPGEE()
        nge = findNGE()

        psee = findPSEE()
        nse = findNSE()

        greater_sum = 0

        smaller_sum = 0

        for i in range(len(nums)):
            greater_contrib = (i - pgee[i]) * (nge[i] - i)
            smaller_contrib = (i - psee[i]) * (nse[i] - i)

            greater_sum = greater_sum + (greater_contrib * nums[i])
            smaller_sum = smaller_sum + (smaller_contrib * nums[i])

        return greater_sum - smaller_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna