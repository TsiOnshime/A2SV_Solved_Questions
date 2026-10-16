class Solution:
    def armstrongNumber (self, n):
        # code here 
        
        num = n
        
        _sum = 0
        
        while n > 0:
            _sum += ((n % 10) ** 3)
            n //= 10
        
        return _sum == num
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna