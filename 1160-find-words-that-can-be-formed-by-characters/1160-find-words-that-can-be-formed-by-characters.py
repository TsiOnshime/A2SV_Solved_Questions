class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}

        sum= 0
        for char in chars:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
    
        for word in words: 
            dic1 = dic.copy()
            for letter in word: 
                if letter not in dic1 or dic1[letter] == 0:
                    break
                dic1[letter] -= 1   
          
            else:
                sum += len(word)

        return sum
