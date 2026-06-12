class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        res = []
        for key, val in count.items():
            if val > n // 3:
                res.append(key)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna