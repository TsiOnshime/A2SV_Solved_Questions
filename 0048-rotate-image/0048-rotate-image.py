class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    # [                               
    #     [0,0] ,[0,1], [0,2] [0,3]
    #     [1,0] ,[1,1], [1,2]
    #     [2,0] ,[2,1], [2,2]
    
    # ]

    # [
    #     [2,0], [1,0], [0,0]         
    #     [2,1], [1,1], [0,1]
    #     [2,2], [1,2], [0,2]

    # ]


        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            for col in range(row + 1,COLS):
                if row == col:
                    continue
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        print(matrix)
        for row in range(ROWS):
            for col in range(COLS//2):
                swapped_col = COLS - 1 - col

                matrix[row][col], matrix[row][swapped_col] = matrix[row][swapped_col], matrix[row][col]


        
