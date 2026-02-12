class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        m x n

          0 1 2
      0  [1,1,1].    if 1,1 == 0 => 0,1 2,1, 1,0, 1,2 
      1  [1,0,1]
      2  [1,1,1]
        """
        rowZero = False
        for m in range(len(matrix)):
            
            for n in range(len(matrix[0])):
                
                
                if matrix[m][n] == 0:
                    
                    matrix[0][n] = 0
                    if m > 0:
                        matrix[m][0] = 0
                    else:
                        rowZero = True
                
      

        for m in range(1,len(matrix)):
            for n in range(1,len(matrix[0])):
                if matrix[0][n] == 0 or matrix[m][0] == 0:
                    matrix[m][n] = 0

        if matrix[0][0] == 0:
            for m in range(len(matrix)):
                matrix[m][0] = 0
        if rowZero:
            for n in range(len(matrix[0])):
                matrix[0][n] = 0