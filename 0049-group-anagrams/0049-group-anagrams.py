class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq_list = defaultdict(list)
        res = []
        for i in range(len(strs)):
            freq = [0] * 26
            offset = ord('a')
            for j in range(len(strs[i])):
                freq[ord(strs[i][j]) - offset] += 1
            freq_list[tuple(freq)].append(strs[i])

        for key, value in freq_list.items():
            res.append(value)
        return res
      


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna