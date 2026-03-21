class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

            for i in range(y, y + k):
                t = x
                b = x + k - 1

                while t < b:
                    grid[t][i], grid[b][i] = grid[b][i], grid[t][i]

                    t += 1
                    b -= 1
            return grid
