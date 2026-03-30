class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        state = []

        def search(i):
            if i == len(nums):
                solution.append(state.copy())
                return
            
            state.append(nums[i])
            search(i + 1)
            state.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            search(i + 1)
        search(0)
        return solution