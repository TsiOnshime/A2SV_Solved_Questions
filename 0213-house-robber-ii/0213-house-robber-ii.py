class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbery(start, end):

            if (start - end + 1) == 1:
                return nums[start]
            prev2 = nums[start]
            prev = max(nums[start + 1], nums[start])

            for i in range(start + 2, end + 1):
                curr = max(prev, nums[i] + prev2)
                prev2, prev = prev, curr

            return prev



        _max = max(robbery(0, len(nums) - 2), robbery(1, len(nums) - 1))

        return _max

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna