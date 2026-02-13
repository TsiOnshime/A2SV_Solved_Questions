class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        # ROWS, COLS = len(img), len(img[0])

        # output = [[0 for i in range(COLS)] for j in range(ROWS)]


        # print(output)

        # for row in range(ROWS):
        #     for col in range(COLS):
                
        #         total = 0
        #         count = 0
        #         for r in range(row - 1 , row + 2):
        #             for c in range(col - 1, col + 2):
        #                 if r < 0 or r == ROWS or c < 0 or c == COLS:
        #                     continue
        #                 total += img[r][c]
        #                 count += 1
                    
        #         output[row][col] = total // count

        # return output




        ROWS, COLS = len(img), len(img[0])


        for row in range(ROWS):
            for col in range(COLS):

                total = 0
                count = 0
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r < 0 or r == ROWS or c < 0 or c == COLS:
                            continue
                        total += img[r][c] % 256
                        count += 1
                img[row][col] = img[row][col] ^ (total // count) << 8

        
        for row in range(ROWS):
            for col in range(COLS):

                img[row][col] = img[row][col] >>  8

        return img
                        