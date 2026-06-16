class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if the strings match / ? decrement i and j
        # if they don't match and the p[j] == * treat that * as empty and move j - 1 or treat * as sequence of characters and move i - 1 but if they don't match and p[j] != * return False

        prev = [float('inf')] * (len(p) + 1) 
        curr = [float('inf')] * (len(p) + 1) 
        prev[0] = True

        
        for j in range(1, len(p) + 1):
            flag = True
            for k in range(j):
                if p[k] != "*":
                    flag = False
            prev[j] = flag

        for i in range(1, len(s) + 1):
            curr[0] = False
            for j in range(1, len(p) + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    curr[j] =  prev[j - 1]
                else:
                    if p[j - 1] != "*":
                        curr[j] = False
                    else:
                        curr[j] = curr[j - 1] or prev[j]
            
            prev = curr.copy()
            
        return prev[len(p)]
                        

 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna