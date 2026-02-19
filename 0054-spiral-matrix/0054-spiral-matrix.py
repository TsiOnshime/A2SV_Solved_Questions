class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r and t < b:
            # get all i's at the top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # get all i's at the right column
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
            # check for 1d matrices
            if l >= r or t >= b:
                return res
            # get all i's at the bottom row
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b -= 1
            # get all i's at the left column

            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res