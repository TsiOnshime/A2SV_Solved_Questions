class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
# [0,1,2,3,4,5,6,9,7]
#                  i 
        while i < n:
            while i < n and nums[i] < n and nums[i] != i:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna