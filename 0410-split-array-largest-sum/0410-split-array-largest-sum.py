class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        low = max(nums)
        high = sum(nums)
        ans = high

        def is_possible(n):
            partition = 1
            _sum = 0
            for i in range(len(nums)):
                if _sum + nums[i] <= n:
                    _sum += nums[i]
                else:
                    _sum = nums[i]
                    partition += 1
            return partition <= k

        while low <= high:
            mid = low + (high - low)//2
            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna