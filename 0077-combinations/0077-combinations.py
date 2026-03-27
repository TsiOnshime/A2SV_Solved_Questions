class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        path = []
        output = []
        def backtrack(i):
            if len(path) == k:
                output.append(path[:])
                return 
            if i > n:
                return 
            path.append(i)
            backtrack(i + 1)
            path.pop()

            backtrack(i + 1)
        
        backtrack(1)
        return output

            