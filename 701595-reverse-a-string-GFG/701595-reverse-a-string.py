#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        s = list(s)
        l = 0 
        r = len(s) - 1
        def reverse(s, l, r):
            
            if l >= r:
                return s
            else:
                s[r], s[l] = s[l], s[r]
            
            return reverse(s, l + 1, r - 1)
            
            
        
        s = reverse(s, l, r)
        return "".join(s)