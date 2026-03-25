class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                powerset.append(subset.copy())
                return
            
            # choose not to include nums[i]
            backtrack(i + 1)
            # choose to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
        


        backtrack(0)
        return powerset


