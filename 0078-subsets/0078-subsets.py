class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, state):
            res.append(state.copy())
            for i in range(start, len(nums)):
                state.append(nums[i])
                dfs(i + 1, state)
                state.pop()

        
        dfs(0, [])
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna