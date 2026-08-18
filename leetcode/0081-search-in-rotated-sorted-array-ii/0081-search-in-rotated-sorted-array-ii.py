class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        [1,0,1,1,1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            # left sorted
            if nums[l] <= nums[mid]:
                if nums[l] == target:
                    return True
                elif nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted
            else:
                if nums[r] == target:
                    return True
                elif nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna