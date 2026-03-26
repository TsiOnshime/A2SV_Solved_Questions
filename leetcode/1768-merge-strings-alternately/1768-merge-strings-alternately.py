class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        merged = []

        p1 = 0
        p2 = 0

        while p1 < n and p2 < m:
            merged.append(word1[p1])
            merged.append(word2[p2])
            p1 += 1
            p2 += 1
        print(p2)
        while p1 < n:
            merged.append(word1[p1])
            p1 += 1

        while p2 < m:
            merged.append(word2[p2])
            p2 += 1

        return "".join(merged)
        
            

