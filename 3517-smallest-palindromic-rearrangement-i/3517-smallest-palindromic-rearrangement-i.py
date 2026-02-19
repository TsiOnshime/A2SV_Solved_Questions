class Solution:
    def smallestPalindrome(self, s: str) -> str:

        count = Counter(s)
        elem = ""
        left_half = []
        
        for char in sorted((count.keys())):

            val = count[char]
            if val % 2 == 1:
                elem = char

            left_half.append(char * (val // 2))

        right_half = ("").join(left_half)

        return right_half + elem + right_half[::-1]
        


            

