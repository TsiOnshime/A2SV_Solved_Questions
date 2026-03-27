class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def is_valid_state(state, j):
            # check the validity
            if len(state) == k:
                return True

    
        
        def get_candidates(j):
            res = []
            for i in range(j, n + 1):
                res.append(i)
            return res

        def search(j):
            if is_valid_state(state, j):               
                solution.append(state.copy())
                return
            
            for candidate in get_candidates(j):
                state.append(candidate)
                search(candidate + 1)
                state.pop()
        
        solution = []
        state = []
        search(1)
        return solution

            
