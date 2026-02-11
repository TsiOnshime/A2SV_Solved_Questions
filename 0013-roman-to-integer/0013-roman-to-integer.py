class Solution:
    def romanToInt(self, s: str) -> int:
      
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0

        i = 0 
        while i < len(s):
            if i + 1 < len(s) and rom[s[i]] < rom[s[i + 1]]:
                
                num += rom[s[i + 1]] - rom[s[i]]
                i += 2
            else:  
                num += rom[s[i]]
                i += 1

        return num
                




