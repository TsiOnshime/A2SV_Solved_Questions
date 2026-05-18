class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Dutch National Flag algo

        target = len(nums) - k

        def quickSelect(l, r):

            low = mid = l
            high = r
            pivot = nums[r]

            while mid <= high:
                if nums[mid] < pivot:
                    nums[mid], nums[low] = nums[low], nums[mid]
                    mid += 1
                    low += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1

            if target < low:
                return quickSelect(l, low - 1)
            elif target > high:
                return quickSelect(high + 1, r)
            else:
                return nums[target]


        return quickSelect(0, len(nums) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna