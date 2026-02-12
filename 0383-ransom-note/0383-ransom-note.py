class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)



        check = ransomNote_counter - magazine_counter

        if len(check):
            return False
        return True
