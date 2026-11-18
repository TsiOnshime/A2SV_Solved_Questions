class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            distinct = set()
            for j in range(i, len(nums)):
                distinct.add(nums[j])
                count += len(distinct) ** 2
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna