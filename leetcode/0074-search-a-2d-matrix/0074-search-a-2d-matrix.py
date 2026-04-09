class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # staircase search

        r = 0
        c = len(matrix[0]) - 1

        while c >= 0 and r < len(matrix):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False