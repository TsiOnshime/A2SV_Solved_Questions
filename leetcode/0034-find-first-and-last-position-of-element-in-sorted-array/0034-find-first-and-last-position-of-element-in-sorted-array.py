class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurence():
            ans = -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] == target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        def last_occurrence():
            ans = -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] == target:
                    ans = mid
                    low = mid + 1
                else:
                    low = mid + 1
            return ans
        
        return [first_occurence(), last_occurrence()]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna