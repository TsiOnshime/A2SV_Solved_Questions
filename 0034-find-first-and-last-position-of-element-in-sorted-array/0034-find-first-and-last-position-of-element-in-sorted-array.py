class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        first = -1
        last = -1
        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if first == -1:
            return [-1, -1]
        l, r = first, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [first, last]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna