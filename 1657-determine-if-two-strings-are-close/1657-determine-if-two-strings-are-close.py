class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_list = [0] * 26
        word2_list = [0] * 26


        offset = ord('a')

        for char in word1:
            word1_list[ord(char) - offset] += 1
        
        for char in word2:
            word2_list[ord(char) - offset] += 1


        if sorted(word1_list) == sorted(word2_list) and set(word1) == set(word2):
            return True
        return False