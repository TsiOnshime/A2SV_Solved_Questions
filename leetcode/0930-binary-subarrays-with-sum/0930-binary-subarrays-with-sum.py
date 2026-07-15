class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count1 = count subarrays whose sum <= goal
        # count2 = subarrays whose sum < goal 
        # subarrays whose sum == goal are count1 - count2
        def findCount(nums, goal):
            if goal < 0:
                return 0

            l, r = 0, 0
            _sum = 0
            count = 0
            while r < len(nums):
                _sum += nums[r]
                while _sum > goal:
                    _sum -= nums[l]
                    l += 1
                if _sum <= goal:
                    count += (r - l + 1)
                r += 1
            return count
        lesser_or_equal = findCount(nums, goal)
        lesser = findCount(nums, goal - 1)
        return lesser_or_equal - lesser


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna