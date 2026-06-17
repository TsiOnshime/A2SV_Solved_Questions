class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        front = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            for j in range(-1, i):
                # take
                take = 0
                if j == -1 or nums[i] > nums[j]:
                    take = 1 + front[i + 1]
                # notake
                notake = front[j + 1]
                val = max(take, notake)
                curr[j + 1] = val   
            front = curr.copy()
        return front[0]           
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna