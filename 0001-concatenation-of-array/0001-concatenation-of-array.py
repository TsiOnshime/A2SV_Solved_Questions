class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        i = 0
        while i < len(ans):
            for j in range(len(nums)):
                 ans[i] = nums[j]
                 i += 1

        return ans