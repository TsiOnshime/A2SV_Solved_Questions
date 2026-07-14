class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        def backtrack(i, state):
            if i == n:
                res = "".join(state)
                if res not in nums:
                    return res
                return 
            state.append("0")
            res = backtrack(i + 1, state)
            if res: 
                return res
            state.pop()

            state.append("1")
            res = backtrack(i + 1, state)
            if res:
                return res
            state.pop()

        
        return backtrack(0, [])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna