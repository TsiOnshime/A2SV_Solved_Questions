class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            # left sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted
            else:
                if nums[mid] <= target and nums[r] >= target:
                    l = mid +  1
                else:
                    r = mid - 1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna