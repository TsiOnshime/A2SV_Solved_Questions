class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # find the first value for which a + b < c 
        count = 0
        nums.sort()

        def find(target, l, r):

            while l <= r:
                mid = l + (r - l)//2

                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return l


        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                target = nums[i] + nums[j]
                k = find(target, j + 1, len(nums) - 1)
                count += k - j - 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna