class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna