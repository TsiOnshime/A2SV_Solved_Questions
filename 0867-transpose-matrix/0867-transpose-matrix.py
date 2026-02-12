class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
       
        ROW, COL = len(matrix), len(matrix[0])
        matrix_t = [[0 for i in range(ROW)] for j in range(COL)]
        
        for row in range(ROW):
            for col in range(COL):
                matrix_t[col][row] = matrix[row][col]

        return matrix_t

        

        