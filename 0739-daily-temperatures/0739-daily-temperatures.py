class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # next greater element
        #  ]

        stack = []
        result = [0] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                result[idx] = i - idx
            
            stack.append(i)

        return result
        

             

