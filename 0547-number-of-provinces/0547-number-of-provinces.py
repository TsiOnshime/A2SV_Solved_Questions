class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
          1 2 3
        1[1,1,0]
        2[1,1,0]
        3[0,0,1]

        unionFind 


        """
        n = len(isConnected)

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1

        provinces = n
        for r in range(n):
            for c in range(n):
                if r != c:
                    if isConnected[r][c] ==1:
                        provinces -= union(r, c)

        return provinces


