class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        temp = num
        count = 0
        while num:
            num >>= 1
            count += 1

        for i in range(count):
            if (temp & (1 << i)) == 0:
                res = res | (1 << i)
        return res


    
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna