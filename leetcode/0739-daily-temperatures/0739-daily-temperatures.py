class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        # next greater element
        #  ]
        answer = [0] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer

        

             

