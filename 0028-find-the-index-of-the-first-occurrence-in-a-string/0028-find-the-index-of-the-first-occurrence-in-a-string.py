class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
we will have two pointers n and h

both start at 0

and we check if hay[h] == ned[n]:
    if they are equal we increment both h and n by 1
    if n == len(ned):
        return 
else: 
    we set n = 0
    if ned[n] == hay[h]:
        n += 1
    h += 1
    sasad
    sad
a and s

        """
# let's save the index of occurences of the first char i in haystack
# iterate through the haystack and save the index in idx list

# we will iterate through the the list idx and initialize h to be i and in the n = 0
# in a while loop h < hay 
        if len(needle) == 0:
            return 0
        idx = []
        for i, ch in enumerate(haystack):
            if ch == needle[0]:
                idx.append(i)
        

        for j in idx:
            h = j
            n = 0

            ned = len(needle) # 5
            hay = len(haystack) # 11

            while h < hay:
                if needle[n] == haystack[h]:
                    h += 1
                    n += 1
                    if n == ned:
                        return h - ned
                else:
                    break
                
        return -1
