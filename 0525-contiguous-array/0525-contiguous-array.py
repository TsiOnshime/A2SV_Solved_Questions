class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _max = 0
        zeroes = 0
        ones = 0
        diff_index = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            elif nums[i] == 1:
                ones += 1
            if zeroes == ones:
                _max = max(_max, i + 1)
            else:
                diff = ones - zeroes
                if diff in diff_index:
                    _max = max(_max, i - diff_index[diff])
                else:
                    diff_index[diff] = i
        return _max

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna