class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        solution = []
        
        def search(i, state, total):
            if total == target:
                solution.append(state[:])
                return

            if i >= n or total > target:
                return 
            
            state.append(candidates[i])
            total += candidates[i]
            search(i, state, total)
            total -= candidates[i]
            state.pop()

            search(i + 1, state, total)
        search(0, [], 0)
        return solution

    
            

            
