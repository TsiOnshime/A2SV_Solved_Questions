class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        
        row_matrix = [0] * (r * c)

        if ROWS * COLS != r * c:
            return mat

        for row in range(ROWS):
            for col in range(COLS):
                new_idx = (row * COLS) + col
                row_matrix[new_idx] = mat[row][col]

        matrix =[]

        for i in range(0,len(row_matrix),c):
            row = row_matrix[i:i+c]
            matrix.append(row)

        return matrix
