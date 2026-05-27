class Solution:
    def intToRoman(self, num: int) -> str:
        
        Int_Rom = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD", 
            100: "C",
            90: "XC", 
            50: "L",
            40: "XL", 
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"

        }

        rom = []
        for key, val in Int_Rom.items():
            freq = num // key
            if freq != 0:
                rom.append(Int_Rom[key] * freq)
            num %= key

        return "".join(rom)

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna