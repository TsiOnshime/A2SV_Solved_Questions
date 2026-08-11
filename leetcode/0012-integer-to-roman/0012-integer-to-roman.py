class Solution:
    def intToRoman(self, num: int) -> str:
        rom_int = {
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
        }
        roman = []
        while num:
            for key, val in rom_int.items():
                quotient = num // val
                if quotient > 0:
                    roman.append(key * quotient)
                    num %= val
                    break
        return "".join(roman)


# 3749
# q = 3
# r = 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna