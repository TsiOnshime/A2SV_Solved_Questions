class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        ans = []
        for i in nums:
            runningSum += i
            ans.append(runningSum)

        return ans