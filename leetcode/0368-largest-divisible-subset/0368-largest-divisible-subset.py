class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
# calculate how many subsets end at each index
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [i for i in range(n)]
        maxi = 0
        lastelem = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                if dp[i] > dp[maxi]:
                    maxi = i
                    lastelem = nums[i]

        ans = []
        i = maxi
        while i != parent[i]:
            ans.append(nums[i])
            i = parent[i]
        ans.append(nums[i])
        return ans





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna