class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = 1 << len(nums)
        res = []
        for number in range(subsets):
            subset = []
            for i in range(len(nums)):
                if number & (1 << i):
                    subset.append(nums[i])
            res.append(subset.copy())
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna