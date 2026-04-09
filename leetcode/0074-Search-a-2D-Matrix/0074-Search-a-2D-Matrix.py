class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for _ in range(row):
            l, r = 0, col - 1

            if target > matrix[_][r]:
                continue

            while l <= r:
                mid = l + (r - l)//2
                if matrix[_][mid] == target:
                    return True
                elif matrix[_][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False