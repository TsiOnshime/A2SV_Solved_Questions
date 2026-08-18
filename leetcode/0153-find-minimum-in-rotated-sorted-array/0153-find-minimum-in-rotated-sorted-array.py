class Solution:
    def findMin(self, nums: List[int]) -> int:
        _min = float('inf')

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[l] <= nums[mid]:
                _min = min(_min, nums[l])
                l = mid + 1
            else:
                _min = min(_min, nums[mid])
                r = mid - 1
        return _min

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna