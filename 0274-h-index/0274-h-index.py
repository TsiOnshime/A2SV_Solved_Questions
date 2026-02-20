class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # [0, 1, 3, 5, 6]
       # {}
       
        # {0:5, 1:4, 3:3, 5:2, 6:1}
        # h-index = 0
        # return if key == val and key > h-index:
        #               h-index = key
        # 
     # {1,1,3}
     # {1:1, 3:1}
# {6,7,8,5,9}
# {}
     # h-idex
        citations.sort()
        
        for i in range(len(citations)):
            # 0 index ?
            remaining = len(citations) - i
            
            if citations[i] >= remaining:
                return remaining
        return 0
# 0 : 5
# 1 : 4
# 2 : 3
# 3 : 3
# 4 : 2
# 5 : 2
# 6 : 1
# 
# [0, 1, 3, 5, 6]

# 0  1   2  3  4
# 0 index -> paper
# ? len - index -> 5 - 0 = 5
# No 

# 1 index -> paper
# ? len - index -> 5 - 1 = 4
# No

# 2 index -> paper
# ? len - index -> 5 - 2 = 3
# Yes -> Return

# 3 index -> paper
# ? len - index -> 5 - 3 = 2
# Yes

# len - idx
# 


