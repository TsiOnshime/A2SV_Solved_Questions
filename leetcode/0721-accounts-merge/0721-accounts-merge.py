class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [0] * n
        email_account = {}
        account_email = {}

        res = []

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return 
            if rank[p1] == rank[p2]:
                parent[p1] = p2
                rank[p2] += 1
            elif rank[p1] < rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2

        for i in range(n):
            m = len(accounts[i])
            for j in range(1, m):
                email = accounts[i][j]
                if email in email_account:
                    union(email_account[email], i)
                    continue
                email_account[email] = i

        for email, acnt in email_account.items():
            p = find(acnt)
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