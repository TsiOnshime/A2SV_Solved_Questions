class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        order = {c:[1,0], b:[1,1], a:[1,0]}
        reserve = [0] * len(s)
        exteded = []
        iterate through s: 
            check if char in order and order[char][0] >= 1:
                if thats the case:
                    reserve[order[char][1]] = char
                    order[char][1] -= 1
            else:
                extended.append(char)
            
            [cba0]
            [d]

        for char in s:
            if char == 0:
                char = extended[0]
                extended.pop(0)

        """
        order_dict = {}
        idx = 0
        for c in order:
            order_dict[c] = idx
            idx += 1
        
        
        return("".join(sorted(s, key=lambda x: order_dict.get(x,100))))