class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combination(i, _sum, state):
            nonlocal res
            if _sum > target:
                return
            if i == len(candidates):
                if _sum == target:
                    res.append(state.copy())
                return
            # no take
            combination(i + 1, _sum, state)
            # take
            state.append(candidates[i])
            _sum += candidates[i]
            combination(i, _sum, state)
            _sum -= candidates[i]
            state.pop()
        combination(0, 0, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna