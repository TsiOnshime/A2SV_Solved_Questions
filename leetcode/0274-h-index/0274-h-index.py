class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        count = [0] * (len(citations) + 1)
      

        for citation in citations:
            if citation >= len(count):
                count[-1] += 1
            else:
                count[citation] += 1


        
        paper_count = 0
        for i in range(len(count) - 1, -1, -1):
            paper_count += count[i]
            if paper_count >= i:
                return i
        return 0