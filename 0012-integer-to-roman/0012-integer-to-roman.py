class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_rom = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10, 
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        result = ""
        for key, value in int_to_rom.items():
            number_of_symbols = num // value
            if (number_of_symbols != 0):
                result += key * number_of_symbols

            num = num % value

        return result 

                    
                

                