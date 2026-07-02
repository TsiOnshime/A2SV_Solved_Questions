class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # [1, 2, 1]

        # [1, 2, 1, 1, 2, 1]
        #  0  1  2  3  4  5
        #  1 + 3 = 4 - 1
        nge = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, i + len(nums)):
                j = j % len(nums)
                if nums[j] > nums[i]:
                    nge[i] = nums[j]
                    break
        return nge




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna