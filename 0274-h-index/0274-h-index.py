class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)

        h = 0

        for i in range(1, n + 1):
            _max = 0


            for j in range(n):

                if citations[j] >= i:
                    _max += 1
                    h_in = i
            if _max >= i:
                h = max(h, h_in)

        return h
