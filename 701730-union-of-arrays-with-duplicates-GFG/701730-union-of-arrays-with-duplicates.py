class Solution:    
    def findUnion(self, a, b):
        # code here
        
        a.extend(b)
        union_array = set(a)
        return union_array
        