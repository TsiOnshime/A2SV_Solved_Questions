class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        power_set = []
        n = len(nums)

        def find_subsets(i, state):
            if i == n:
                power_set.append(state.copy())
                return 
            # no pick
            find_subsets(i + 1, state)

            # pick
            state.append(nums[i])
            find_subsets(i + 1, state)
            state.pop()
        
        find_subsets(0, [])
        return power_set

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna