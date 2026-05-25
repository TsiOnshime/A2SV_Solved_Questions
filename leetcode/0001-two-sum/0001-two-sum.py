class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.index = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in self.index and i != self.index[complement]:
                return [i, self.index[complement]]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna