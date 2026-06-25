class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, state):
            if i == len(nums):
                res.append(state.copy())
                return
            
            state.append(nums[i])
            dfs(i + 1, state)
            state.pop()

            dfs(i + 1, state)
        
        dfs(0, [])
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna