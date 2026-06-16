class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        prev = [0] * (len(word2) + 1)
        curr = [0] * (len(word2) + 1)

        for j in range(len(word2) + 1):
            prev[j] = j
  
        for i in range(1, len(word1) + 1):
            curr[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    ins = 1 + curr[j - 1]
                    dele = 1 + prev[j]
                    rep = 1 + prev[j - 1]
                    curr[j] = min(ins, dele, rep)
            prev = curr.copy()

        return prev[len(word2)]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna