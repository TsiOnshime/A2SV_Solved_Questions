class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4':["g", "h", "i"], '5':["j", "k","l"], '6':["m", "n", "o"], '7':["p", "q", "r","s"], '8':["t", "u", "v"], '9':["w", "x", "y", "z"]}

        solution = []
        state = []

        def search(i):
            if len(state) == len(digits):
                solution.append("".join(state.copy()))
                return

            possibilities = mapping[digits[i]]
            for char in possibilities:
                state.append(char)
                search(i + 1)
                state.pop()
        search(0)
        return solution
