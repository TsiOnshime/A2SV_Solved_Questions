from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic =
        # {

        #     (frequecy of each element): [the strings]
        # }
        # _dict = defaultdict(list)
     
        # arr = [0] * 26
        
        # iterate throu the strings
        #     for letter in string
        #         i would increase teh value of its index at arr
        #     _dict[tuple(arr)].append(string)

        #  strs = ["eat","tea","tan","ate","nat","bat"]

        #  arr = [1,0,0,0,1--------1000000]
        #  {
        #     (1,0,0,0,1--------1000000): ["eat","tea"],
        #     (1,0,0,,,0,0,1, -----1,0,0,0): ["tan"]
        #  }
            
        # return [_dict.values] [["eat","tea"], "tan"]


        _dict = defaultdict(list)

        
        for word in strs:
            arr = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                arr[index] += 1
            _dict[tuple(arr)].append(word)

        return [i for i in _dict.values()]



        
