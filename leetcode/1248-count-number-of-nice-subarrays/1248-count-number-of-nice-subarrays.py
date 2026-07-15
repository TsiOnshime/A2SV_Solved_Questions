class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def countSubarrays(nums, k):
            if k < 0:
                return 0
            l, r = 0, 0
            count = 0
            odds = 0

            while r < len(nums):
                if nums[r] & 1:
                    odds += 1
                while odds > k:
                    if nums[l] & 1:
                        odds -= 1
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        
        count1 = countSubarrays(nums, k)
        count2 = countSubarrays(nums, k - 1)
        return count1 - count2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna