class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def countSubarrays(nums, k):
            if k == 0:
                return 0

            l, r = 0, 0
            chars = {}
            count = 0

            while r < len(nums):
                if nums[r] not in chars:
                    chars[nums[r]] = 1
                else:
                    chars[nums[r]] += 1
                while len(chars) > k:
                    chars[nums[l]] -= 1
                    if chars[nums[l]] == 0:
                        del chars[nums[l]]
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        return countSubarrays(nums, k) - countSubarrays(nums, k - 1)

      

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna