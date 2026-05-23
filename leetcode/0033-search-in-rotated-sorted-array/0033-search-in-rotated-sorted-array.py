class Solution:
    def search(self, nums: List[int], target: int) -> int:
# find the pivot where nums[p - 1] < nums[p] < nums[p + 1]
# if target > nums[l] search (l:p)
# if target < nums[r] search(p:r)


# calculate mid

# check if it is in the left sorted array
#  how? if nums[l] < nums[mid]: we are in the left sorted array
#        check if our target belongs in that sub array how? if nums[l] < target: r = mid - 1
#         else: l = mid + 1

# else: we are on the right sorted array:
#       if nums[mid] < target < nums[r]: l = mid + 1
#       else: r = mid - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r =mid - 1

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna