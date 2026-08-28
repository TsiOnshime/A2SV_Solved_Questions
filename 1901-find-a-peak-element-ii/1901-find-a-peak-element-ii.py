class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        def findMax(mid):
            idx, _max = -1, -1
            for i in range(rows):
                if mat[i][mid] > _max:
                    _max = mat[i][mid]
                    idx = i
            return [idx, _max]

        l, r = 0, cols - 1
        while l <= r:
            mid = l + (r - l)//2
            idx, _max = findMax(mid)
            l1 = mat[idx][mid - 1] if mid - 1 >= 0 else float('-inf')
            l2 = mat[idx][mid + 1] if mid + 1 < cols else float('-inf')

            if l1 < mat[idx][mid] > l2:
                return [idx, mid]
            elif l1 > mat[idx][mid]:
                r = mid - 1
            else:
                l = mid + 1
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna