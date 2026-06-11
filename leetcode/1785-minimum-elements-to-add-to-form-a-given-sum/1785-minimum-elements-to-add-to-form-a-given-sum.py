class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(goal-(sum(nums)))+limit-1) // limit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna