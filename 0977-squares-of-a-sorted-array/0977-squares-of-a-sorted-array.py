class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        l, r = 0, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                l = i
        r = l + 1
        while l >= 0 and r < len(nums):
            a = abs(nums[l])
            b = abs(nums[r])
            if a < b:
                arr.append(a ** 2)
                l -= 1
            else:
                arr.append(b ** 2)
                r += 1
        while l >= 0:
            arr.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            arr.append(nums[r] ** 2)
            r += 1
        
        return arr

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna