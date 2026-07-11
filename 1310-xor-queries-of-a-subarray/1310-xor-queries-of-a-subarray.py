class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
# 0110
# 0001
# 0111
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
       

        ans = []
        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1]

            left = prefix[l - 1] if l > 0 else 0
            right = prefix[r]
            
            ans.append(left ^ right)
        
        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna