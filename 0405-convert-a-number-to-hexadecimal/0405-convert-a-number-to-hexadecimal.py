class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        
        if num<0:
            num+=2**32

        digits = "0123456789abcdef"
        ans = ""

        while num:
            remender=num%16
            ans=digits[remender]+ans
            num//=16

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna