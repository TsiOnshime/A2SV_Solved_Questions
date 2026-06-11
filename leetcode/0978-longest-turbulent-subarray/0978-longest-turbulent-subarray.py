class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        prev = ""
        res = 1

        l, r = 0, 1

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            else:
                r = r + 1 if arr[r-1] == arr[r] else r
                l = r - 1
                prev = ""

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna