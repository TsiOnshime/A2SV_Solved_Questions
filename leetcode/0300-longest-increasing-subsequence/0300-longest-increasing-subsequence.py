class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        def search(arr, target):

            l = 0
            r = len(arr) - 1
 
            while l <= r:
                mid = l + (r - l)//2
                if arr[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1
            return l

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                idx = search(res, nums[i])
                res[idx] = nums[i]
        return len(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna