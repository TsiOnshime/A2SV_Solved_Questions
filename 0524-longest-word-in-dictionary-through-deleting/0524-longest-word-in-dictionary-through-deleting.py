class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # abpcplea
        # ale => yes
        # apple => yes
        # "monkey" => no
        # plea => yes
        # filter based on length
        # filter based on lexicographical order
        output = []
        s_p = 0
        d_p = 0

        for i in range(len(dictionary)):        
            s_p = 0
            d_p = 0
            word = dictionary[i]
            while s_p < len(s):
                if s[s_p] == word[d_p]:
                    d_p += 1
                s_p += 1
                if d_p == len(word):
                    output.append(word)
                    break
        if len(output) == 0:
            return ""
        max_length = len(output[0])
        for i in output:
            max_length = max(max_length, len(i))
        length_filtered = []
        for i in output:
            if len(i) == max_length:
                length_filtered.append(i)
     

        return min(length_filtered)

