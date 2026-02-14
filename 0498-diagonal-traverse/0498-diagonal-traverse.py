class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(mat), len(mat[0])


        res = []

        going_up = True

        cur_row, cur_col = 0, 0

        while len(res) != (ROWS * COLS):
            if going_up:
                while cur_row >= 0 and cur_col < COLS:
                    res.append(mat[cur_row][cur_col])

                    cur_row -= 1
                    cur_col += 1

                
                if cur_col == COLS:
                    cur_col -= 1
                    cur_row += 2

                else:
                    cur_row += 1

                going_up = False
            else:
                while cur_col >= 0 and cur_row < ROWS:
                    res.append(mat[cur_row][cur_col])

                    cur_row += 1
                    cur_col -= 1

                if cur_row == ROWS:
                    cur_col += 2
                    cur_row -= 1

                else:
                    cur_col += 1
                going_up = True

        return res

            


            
            

            


