class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        state = []
        def search(i):
            if i >= len(nums):
                solution.append(state.copy())
                return
            
            # decision to include nums[i]
            state.append(nums[i])
            search(i + 1)

            # decision not to include nums[i]
            state.pop()
            search(i + 1)

        search(0)
        return solution
