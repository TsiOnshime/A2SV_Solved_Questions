class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        email_idx = {}

        uf = UnionFind(n)

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in email_idx:
                    uf.union(email_idx[email], i)
                else:
                    email_idx[email] = i

        parent_email = defaultdict(list)

        for email, idx in email_idx.items():
            uParent = uf.find(idx)
            parent_email[uParent].append(email)
        
        output = []
        for idx, emails in parent_email.items():
        
            account = [accounts[idx][0]] + sorted(emails)
            output.append(account)

        return output

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna