class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #[0,0,0,0,0,0,0,0,0,0,0,0,0]
        #[-1,2,-1]
        #[1,-1,1]
        #[1,1,0]
        # [0, -1,0]
        #[1,0,0]
        #[-1, -1, 0, 0, 0,0,0,0]
        #[0, 1, 0, -1]
        #[0, 1, 1, 0]
        #[-1,0, 1, 0]
        # we keep count of the freq array which starts at 0 and end at 25
        # for each shift in shifts first we check the value of shift[2] 
        # if it is 0 we change the value at freq[shift[0]] -= 1
        # freq[shift[1]+1] += 1
        # elif it is 1 we we change the value at freq[shift[0]] += 1
        # freq[shift[1]+1] -= 1
        # we then calculate the prefix_sum of the freq
        # then we iterate through the string and shift it by the value at that index

        # freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # freq = -1, 0, 1
        # freq = [0,1,1,0]
        # pref = [0, 1, 2, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # s = "abc"
        # char = chr((ord(char) + pref[ord(char)- offset]) % 123)
        
        # s = "ace"
 
        freq = [0] * (500005)
        for shift in shifts:
            start,end, d = shift[0], shift[1], shift[2]
            if d == 0:
                freq[start] -= 1
                freq[end + 1] += 1
            else:
                freq[start] +=1
                freq[end + 1] -= 1

        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]
      
        offset = 97
        shift = [0] * len(s)
        for i in range(len(s)):
            shift[i] = chr(((ord(s[i]) - offset + freq[i]) % 26 + 97))
            
        return "".join(shift)
        
