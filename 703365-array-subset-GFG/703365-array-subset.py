#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here

        counter_a = {}
        counter_b = {}
        
        for i in range(len(a)):
            if a[i] not in counter_a:
                counter_a[a[i]] = 1
                continue
            counter_a[a[i]] += 1
            
        for i in range(len(b)):
            if b[i] not in counter_b:
                counter_b[b[i]] = 1
                continue
            counter_b[b[i]] += 1
            
        for key in counter_b:
            if key not in counter_a:
                return False

            if counter_a[key] < counter_b[key]:
                return False
        return True
        
            
    
    
    
    
