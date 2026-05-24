class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        if len(nums) < 3:
            return 0
# 0, 1, 2
        nums.sort()
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1

            while left <= right:
                target = nums[i]

                if nums[left] + nums[right] > target:
                    count += right - left
                    right -= 1
                else: 
                    left += 1

        return count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna