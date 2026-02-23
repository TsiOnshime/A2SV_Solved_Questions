class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        elem = rows * cols

        T = rStart
        B = T + 1
        L = cStart
        R = cols - 1

        while len(res) < elem:

            # left to right
            if T >= 0:
                for i in range(L, cols):
                    res.append([T, i])
                T -= 1
                L -= 1
            # Top to bottom
            if R < cols:
                for i in range(T, B+1):
                    res.append([i, R - 1])
                
                R += 1
            # Right to Left
            if L >= 0:
                for i in range(cols - 1, L - 1, - 1):
                    res.append([B, i])
                B += 1
            # Bottom to Top
            if B < rows:
                for i in range(B, -1,-1):
                    res.append([i, L])
        print(res)