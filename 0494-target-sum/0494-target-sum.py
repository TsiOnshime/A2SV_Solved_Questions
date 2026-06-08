class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
   
        dp = {}

        def searchWays(i, _sum):
          
            if i == len(nums):
                if _sum == target:
                    return 1
                return 0
            
            if (i, _sum) in dp:
                return dp[(i, _sum)]

            num = nums[i]

            plus = searchWays(i + 1, _sum + num)
            minus = searchWays(i + 1, _sum - num)
            
            dp[(i, _sum)] = plus + minus

            return plus + minus
            

        
        return searchWays(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna