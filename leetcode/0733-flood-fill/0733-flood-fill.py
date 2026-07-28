class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(image), len(image[0])

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == original and (r, c) not in visited:
                return True
            return False
            
        def dfs(r, c):

            visited.add((r, c))
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if is_valid(nr, nc):
                    dfs(nr, nc)
        dfs(sr, sc)
        return image



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna