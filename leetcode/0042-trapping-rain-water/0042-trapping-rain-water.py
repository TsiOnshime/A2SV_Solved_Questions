class Solution:
    def trap(self, height: List[int]) -> int:



        rain = 0
        prefix_max = [height[0]] * len(height)
        suffix_max = [height[-1]] * len(height)
        
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
            
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])
            
        for i in range(len(height)):
            if height[i] < prefix_max[i] and height[i] < suffix_max[i]:
                rain += min(prefix_max[i], suffix_max[i]) - height[i]
        return rain
        
    # [3, 0, 1, 0, 4, 0, 2]
    
    # [4, 0, 2]
    
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna