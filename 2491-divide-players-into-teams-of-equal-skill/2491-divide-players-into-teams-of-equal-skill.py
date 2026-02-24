class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = []
        n = len(skill)
        ch = n // 2

        summ = skill[0] + skill[-1]
        curr_sum = 0

        i = 0 
        j = n - 1

        for _ in range(ch):
            curr_sum = skill[i] + skill[j]
            if summ == curr_sum:
                chemistry.append((skill[i], skill[j]))
                i += 1
                j -= 1
            else:
                return -1
        
        sum_ch = 0

        for l, r in chemistry:
            sum_ch += (l * r)

        return sum_ch
        