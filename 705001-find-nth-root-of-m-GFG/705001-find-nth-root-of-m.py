class Solution:
    def nthRoot(self, n, m):
        l, r = 0, m
        
        while l <= r:
            mid = l + (r - l)//2
            
            num = 1
            for i in range(n):
                num *= mid
            
            if num == m:
                return mid
            elif num > m:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
       


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna