class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbery(start, end, dp):
            if end <= start:
                return nums[start]
            if end == start + 1:
                return max(nums[start], nums[end])

            if dp[end] != -1:
                return dp[end]

            take = nums[end] + robbery(start, end - 2, dp)
            notake = robbery(start, end - 1, dp)

            val = max(take, notake)

            dp[end] = val

            return val



        for i in range(2):
            dp = [-1] * len(nums)
            if i == 0:
                _max = robbery(0, len(nums) - 2, dp)
                print(_max)
            else:
                _max = max(_max, robbery(1, len(nums) - 1, dp))

        return _max



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna