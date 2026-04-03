class Solution:
    def smallestNumber(self,pattern):


        visited = set()
        possibilities = []
        state = []

        def solve():
            search()
            return possibilities
        
        def is_valid_state():
            if len(visited) == len(pattern) + 1:
                return True
        def get_candidates():
            res = []
            for i in range(1, len(pattern) + 2):
                if i not in visited:
                    res.append(i)
            return res
        def search():
            if is_valid_state():
                k = 0
                p = 0
                s = 0
                while p < len(pattern) and k + 1 < len(state):
                    if pattern[p] == "I":
                        if state[k] < state[k + 1]:
                            p += 1
                            k += 1
                        else:
                            break
                    elif pattern[p] == "D":
                        if state[k] > state[k + 1]:
                            p += 1
                            k += 1
                        else:
                            break
                    if p == len(pattern):
                        possibilities.append(state.copy())
                        break
                return 
            for candidate in get_candidates():
                state.append(candidate)
                visited.add(candidate)
                search()
                visited.remove(candidate)
                state.remove(candidate)
        solve()


        return "".join(str(i) for i in possibilities[0][0:len(pattern) + 1])
o = Solution()
print(o.smallestNumber("DDDIII"))
            