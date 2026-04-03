class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # to make my lookup faster
        wordDict = set(wordDict)

        sentences = []
        state = []

        def solve():
            search(0)
            return sentences

        # i => my start index
        # j => my end index
        def search(i):

            if i == len(s):
                sentences.append(" ".join(state.copy()))
                return

            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]

                if substring in wordDict:
                    state.append(substring)
                    search(j)
                    state.pop()
        return solve()

