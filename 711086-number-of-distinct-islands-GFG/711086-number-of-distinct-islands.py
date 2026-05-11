#User function Template for python3

import sys
from collections import deque
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        distinct = set()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == 1:
                return True
            return False
    
        def bfs(r, c):
            island = set()
            br, bc = r, c
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            island.add((0, 0))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if is_valid(nr, nc):
                        island.add((nr - br, nc - bc))
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return tuple(sorted(island))
            
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island = bfs(r, c)
                    distinct.add(island)
                    
        return len(distinct)
        
        