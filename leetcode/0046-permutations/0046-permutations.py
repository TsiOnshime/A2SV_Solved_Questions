class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def permutiations(used, state):
            if len(used)== len(nums):
                res.append(state.copy())
                return
            
            for i in range(len(nums)):
                if i not in used:
                    state.append(nums[i])
                    used.add(i)
                    permutiations(used, state)
                    used.remove(i)
                    state.pop()

        permutiations(set(), [])
        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna