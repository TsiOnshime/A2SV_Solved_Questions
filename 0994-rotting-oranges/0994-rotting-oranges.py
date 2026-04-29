class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        noRot = False

       

        def rotFruit(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] != 1:
                return 
            queue.append((r, c))
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    noRot = True
        if not noRot:
            return 0
        
        
        
        
        time = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                rotFruit(r - 1, c)
                rotFruit(r + 1, c)
                rotFruit(r , c- 1)
                rotFruit(r, c + 1)

            time += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time -1
