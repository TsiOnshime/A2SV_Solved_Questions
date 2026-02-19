class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        m = len(mat)
        n = len(mat[0])
        
        for i in range(4):
            for r in range(m):
                for c in range(r+1,n):
                    if r == c:
                        continue

                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            
            for r in range(m):
                for c in range(n//2):
                    swapped_col = n - 1 - c

                    mat[r][c], mat[r][swapped_col] = mat[r][swapped_col], mat[r][c]
            
            if mat == target:
                return True
        return False
                
