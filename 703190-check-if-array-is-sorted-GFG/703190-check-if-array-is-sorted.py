class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        if len(arr) == 1:
            return True
        l = 0
        r = 1
        
        while r < len(arr):
            if arr[r] < arr[l]:
                return False
            r += 1
            l += 1
        return True
                