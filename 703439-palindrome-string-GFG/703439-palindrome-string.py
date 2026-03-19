class Solution:
    def isPalindrome(self, s):
        # code here
        
        def palindrome(l, r):
            if l > r:
                return True
            
            if s[l] != s[r]:
                return False
                
            return palindrome(l + 1, r - 1)
        
        return palindrome(0, len(s) - 1)
            
        
        
