class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        in_s = s_counter - t_counter
       
        changing_letters = [values for values in in_s.values()]

        print(changing_letters)
        return sum(changing_letters)
        # print(s_counter - t_counter)
        # print(t_counter - s_counter)

        # print((s_counter - t_counter).values())
        # print((t_counter - s_counter).values())

     

