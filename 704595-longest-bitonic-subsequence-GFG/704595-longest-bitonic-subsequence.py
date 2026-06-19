from typing import List
class Solution:
    def longestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        
        # find lis for nums starting from 0 - n
        # find lis for nums starting from n-1 - -1
        # add the values at an index - 1 to find the number of elements
        
        res1 = [1] * n
        res2 = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    res1[i] = max(res1[i], res1[j] + 1)
                
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    res2[i] = max(res2[i], res2[j] + 1)
                
    
        _max = 0
        # [5, 7, 9]
        # [1, 2, 3]
        # [1, 1, 1]
        
        for i in range(n):
            if res1[i] > 1 and res2[i] > 1:
                val = res1[i] + res2[i] - 1
                _max = max(val, _max)
            
        return _max 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna