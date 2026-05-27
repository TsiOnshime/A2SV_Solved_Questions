class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
        
    def find(self,node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
            node = self.parent[node]
        return node

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return 
            
        if self.rank[p1] == self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 1: left, right
        # 2: up, down
        # 3: left, down
        # 4: right, down
        # 5: left, up
        # 6: right, up

        # 1: [3, 4, 5, 6]
        # 2: [3, 4, 5, 6]
        # 3: [1, 2, 4, 5]
        # 4: [1, 2, 3, 5]
        # 5: [1, 2, 4, 6]
        # 6: [1, 2, 4, 5]
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)




        # 1: left, right
        # 2: up, down
        # 3: left, down
        # 4: right, down
        # 5: left, up
        # 6: right, up
        def getId(r, c):
            return r * cols + c

        def detectLeft(r, c):
            if c - 1 >= 0  and grid[r][c - 1] in {1, 4, 6}:
                uf.union(getId(r, c), getId(r, c - 1))
            
        def detectRight(r, c):
            if c + 1 < cols and grid[r][c + 1] in {1, 3, 5}:
                uf.union(getId(r, c), getId(r, c + 1))

        def detectUp(r, c):
            if r - 1 >= 0 and grid[r - 1][c] in {2, 3, 4}:
                uf.union(getId(r, c), getId(r - 1, c))
        
        def detectDown(r, c):
            if r + 1 < rows and grid[r+1][c] in {2, 5, 6}:
                uf.union(getId(r, c), getId(r + 1, c))

        def handler(r, c):
            if grid[r][c] == 1:
                detectLeft(r,c)
                detectRight(r,c)
            elif grid[r][c] == 2:
                detectUp(r,c)
                detectDown(r,c)
            elif grid[r][c] == 3:
                detectLeft(r, c)
                detectDown(r, c)
            elif grid[r][c] == 4:
                detectRight(r, c)
                detectDown(r, c)
            elif grid[r][c] == 5:
                detectLeft(r, c)
                detectUp(r, c)
            else:
                detectRight(r, c)
                detectUp(r, c)





        for r in range(rows):
            for c in range(cols):
                handler(r, c)

        return uf.find(getId(0, 0)) == uf.find(getId(rows - 1, cols - 1))
        # def handler(r, c, neigh):
        #     if not is_valid(r, c):
        #         return 
            

            


        




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna