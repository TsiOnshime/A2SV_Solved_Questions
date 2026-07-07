class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    
    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
        
    def union(self, slot):
        self.parent[slot] = self.find(slot - 1)
        
class Solution:
    def jobSequencing(self, deadline, profit):
        max_profit = 0
        count = 0
        uf = UnionFind(max(deadline) + 1)
        for i in range(len(profit)):
            profit[i] = [profit[i], deadline[i]]
        profit.sort(reverse=True)
        

        for i in range(len(profit)):
            p, d = profit[i]
         
            slot = uf.find(d)
            if slot != 0:
                count += 1
                max_profit += p
                uf.union(slot)
    
      
        return [count, max_profit]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna