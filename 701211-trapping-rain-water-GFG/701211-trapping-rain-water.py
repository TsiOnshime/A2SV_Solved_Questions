class Solution:
    def maxWater(self, arr):

        rain = 0
        prefix_max = [arr[0]] * len(arr)
        suffix_max = [arr[-1]] * len(arr)
        
        for i in range(1, len(arr)):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])
            
        for i in range(len(arr) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], arr[i])
            
        for i in range(len(arr)):
            if arr[i] < prefix_max[i] and arr[i] < suffix_max[i]:
                rain += min(prefix_max[i], suffix_max[i]) - arr[i]
        return rain
        
    # [3, 0, 1, 0, 4, 0, 2]
    
    # [4, 0, 2]
    
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna