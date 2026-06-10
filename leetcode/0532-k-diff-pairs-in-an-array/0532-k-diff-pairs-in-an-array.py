class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        print(nums)
        l = 0
        r = 1
        temp = 0
        while r < len(nums):
            if nums[r] == nums[r - 1] and r - 1 != l:
                r += 1
                continue

            diff = nums[r] - nums[l]
            if diff == k:
                count += 1
                temp = r
            elif diff > k:
                l += 1
                while l < len(nums) and nums[l] == nums[l - 1]:
                    l += 1
                r = temp if temp and temp > l else l + 1
                continue
            r += 1
        return count
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna