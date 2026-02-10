class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = list(s)
        combined = list(zip(s_list, indices))
        

        shuffled = [0] * len(s)


        for letter, index in combined:
            
            shuffled[index] = letter
        return ("").join(shuffled)