class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        _sum = 0
        original_sum = (n * (n + 1))//2
        squared_sum = 0
        original_square_sum = (n * (n + 1) * ((2 * n) + 1))//6

        for i in range(n):
            _sum += nums[i]
            squared_sum += nums[i] ** 2

        sum_diff = _sum - original_sum # r - m
        squared_sum_diff = squared_sum - original_square_sum # r^2 - m^2

        values_sum = (squared_sum_diff) // sum_diff # r + m

        # sum_diff + values_sum = 2r 
        r = (sum_diff + values_sum) // 2
        m = values_sum - r

        return [r, m]





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna