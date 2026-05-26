class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def explore(start, i, path):
            r, c = start
            if i >= len(word):
                return True          
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in path or board[r][c] != word[i]:
                return
            path.add((r, c))

            for dr, dc in directions:
                if explore((r + dr, c + dc), i + 1,path):
                    return True
               
            path.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if explore((r, c), 0, set()):
                        return True

        return False


            


        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna