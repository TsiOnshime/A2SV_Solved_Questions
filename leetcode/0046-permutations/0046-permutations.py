class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

       
        def is_valid_state(state):
            # check if it is a valid state
            if len(state) == len(nums):
                return True

        
        def get_candidates(state):
            res = []
            for i in range(len(nums)):
                if used[i] == False:
                    res.append(nums[i])
            return res

        
        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state[:])
            
            for candidate in get_candidates(state):
                state.append(candidate)
                used[nums.index(candidate)] = True
                search(state, solutions)
                state.remove(candidate)
                used[nums.index(candidate)] = False
        
        
        used = [False] * len(nums)
        state = []
        solutions = []
        search(state, solutions)
        return solutions
            
        