class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        _min, _max = matrix[0][0], matrix[rows - 1][cols - 1]

        ans = -1 
        while _min <= _max:
            mid = _min + (_max - _min) // 2
            count = self.smaller_elements_count(matrix, mid, rows, cols)
            if count >= k:
                ans = mid
                _max = mid - 1
            else:
                _min = mid + 1
        return ans


    def smaller_elements_count(self, matrix, elem, rows, cols):
        count = 0
        for n in range(rows):
            l = 0
            r = cols - 1
            while l <= r:
                mid = l + (r - l)//2
                if matrix[n][mid] > elem:
                    r = mid - 1
                else:
              
                    l = mid + 1

            count += l
        print(count)

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna