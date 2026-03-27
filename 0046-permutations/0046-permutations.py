class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def backtrack(nums):
            if not nums:
                ans.append(path.copy())

            for i in nums:
                path.append(i)

                potential_candidate = nums[:]
                potential_candidate.remove(i)
                backtrack(potential_candidate)
                path.pop()
        

        backtrack(nums)
        return ans