class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def is_valid(val):
            num = 0
            for i in range(len(nums)):
                num += math.ceil(nums[i]/val)
            return num <= threshold
       
        ans = sum(nums)
        l, r = 1, max(nums)
        while l <= r:
            mid = l + (r - l)//2
            if is_valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna