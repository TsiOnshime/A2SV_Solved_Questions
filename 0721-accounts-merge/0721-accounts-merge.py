class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return 
        if self.rank[p1] == self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_account = {}
        account_email = {}

        res = []

        for i in range(n):
            m = len(accounts[i])
            for j in range(1, m):
                email = accounts[i][j]
                if email in email_account:
                    uf.union(email_account[email], i)
                    continue
                email_account[email] = i

        for email, acnt in email_account.items():
            p = uf.find(acnt)
            if p in account_email:
                account_email[p].append(email)
            else:
                account_email[p] = [email]
        full_info = []
        for acnt, email in account_email.items():
            email = sorted(email)
            name = [accounts[acnt][0]]
            name.extend(email)
            full_info.append(name)
        return full_info


            

        

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna