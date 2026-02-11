class Solution:
    def frequencySort(self, s: str) -> str:
        
            ls = [0] * 128
            new_string = list()
            for char in s:
                ls[ord(char)] += 1
            
            for i in range(len(s)):

                maxx = max(ls)
                if maxx == 0:
                    break
                new_string.append(chr(ls.index(maxx)) * maxx)
                ls[ord(chr(ls.index(maxx)))] = 0

            return ("").join(new_string)

