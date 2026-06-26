class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutiations(i, state):
            if i == len(nums):
                res.append(state.copy())
                return 
            
            for ind in range(i, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                state.append(nums[i])
                permutiations(i + 1, state)
                state.pop()
                nums[i], nums[ind] = nums[ind], nums[i]

        permutiations(0, [])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna