class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        candidates = {
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["b", "a"]

        }

        offset = ord('a')
        solution = []
        state = []
  

        def solve():
            search(0)
            

        def is_valid_state(i):
            if len(state) == n:
                return True
            if i > n:
                return 
        def get_candidates(i):
            if i == 0:
                return ["a", "b", "c"]
            return candidates[chr(((ord(state[-1]) - offset) % 3) + offset)]
        def search(i):
            if is_valid_state(i):
                solution.append(state.copy())
                return
            for candidate in get_candidates(i):
                
                state.append(candidate)
                search(i + 1)
                state.pop()
        solve()
        solution.sort()
        for i in range(len(solution)):
            if i == k - 1:
                return "".join(solution[i])
        else:
            return ""



