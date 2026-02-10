class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_counter = Counter(s)
        # t_counter = Counter(t)
        
        # if s_counter == t_counter:
        #     return True
        # return False

        count = defaultdict(int)

        for char in s: 
            count[char] += 1
        for char in t:
            count[char] -= 1

        for char in count:
            if count[char] != 0:
                return False
        return True


       