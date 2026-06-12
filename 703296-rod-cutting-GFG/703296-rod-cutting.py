#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        # length = len(price)
        # length = i + 1
        prev = [float('-inf')] * (len(price) + 1)
        
        for i in range(len(price) + 1):
            prev[i] = (i) * price[0]
            
        for i in range(1, len(price)):
            for length in range(len(price) + 1):
                notake = 0 + prev[length]
                take = float('-inf')
                if i + 1 <= length:
                    take = price[i] + prev[length - (i + 1)]
                    
                prev[length] = max(notake, take)
                
        return prev[len(price)]
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna