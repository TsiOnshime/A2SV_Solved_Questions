class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ans = letters[0]
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = l + (r - l)//2
        
            if ord(target) < ord(letters[mid]):
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans
# ["x","x","y","y"] target = "z"
# l = 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna