class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4':["g", "h", "i"], '5':["j", "k","l"], '6':["m", "n", "o"], '7':["p", "q", "r","s"], '8':["t", "u", "v"], '9':["w", "x", "y", "z"]}
        solution = []
        state = []

        def solve():

            search(0)
            return solution
        def is_valid_state(i):
            if len(state) == len(digits):
                solution.append("".join(state.copy()))
            return i == len(digits)

        def get_candidates(i):
            return mapping[digits[i]]
        
        def search(i):
            if is_valid_state(i):
                return

            for candidate in get_candidates(i):         
                state.append(candidate)
                search(i + 1)
                state.pop()
        return solve()

