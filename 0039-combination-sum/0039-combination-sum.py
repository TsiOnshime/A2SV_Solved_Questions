class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []
        def combinations(i, _sum, state):
            if _sum > target:
                return 
            if i == len(candidates):
                if _sum == target:
                    res.append(state.copy())
                return 
            # not pick
            combinations(i + 1, _sum, state)
            # pick
            _sum += candidates[i]
            state.append(candidates[i])
            combinations(i , _sum, state)
            _sum -= candidates[i]
            state.pop()
        
        combinations(0, 0, [])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna