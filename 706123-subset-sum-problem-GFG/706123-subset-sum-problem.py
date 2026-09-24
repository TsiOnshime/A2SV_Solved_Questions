class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        cache = {}
        def find_subset(i, currSum):
            if currSum == sum:
                return True
            if i >= len(arr) or currSum > sum:
                return False
            if (i, currSum) in cache:
                return cache[(i, currSum)]
                
            not_take = find_subset(i + 1, currSum)
            if not_take:
                cache[(i, currSum)] = True
                return True
                
            take = find_subset(i + 1, currSum + arr[i])
            
            cache[(i, currSum)] = take
            return take
        
        if find_subset(0, 0):
            return True
        return False
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna