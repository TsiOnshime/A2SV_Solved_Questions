class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def permutiations(nums, state):
            if not nums:
                res.append(state.copy())
                return
            
            for i in range(len(nums)):
                state.append(nums[i])
                new_nums = nums[:i] + nums[i + 1:]
                permutiations(new_nums, state)
                state.pop()

        permutiations(nums, [])
        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna