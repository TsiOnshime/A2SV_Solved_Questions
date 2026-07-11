class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual = 0
        for i in range(len(nums)):
            actual ^= nums[i]
        
        def xorAllNumbers(n):     
            if n % 4 == 0:
                return n
            if n % 4 == 1:
                return 1
            if n % 4 == 2:
                return n + 1
            else: 
                return 0

        expected = xorAllNumbers(len(nums))
        print(expected)
        res = actual ^ expected
        return res



# 0 ^ 1 = 1
# 0 ^ 1 ^ 2 = 3
# 0 ^ 1 ^ 2 ^ 3 = 0
# 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 = 7
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 = 0
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 = 1
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10 = 11
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10 ^ 11 = 0
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10 ^ 11 ^ 12 = 12
# 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10 ^ 11 ^ 12 ^ 13 = 1 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna