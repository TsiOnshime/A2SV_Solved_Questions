class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        res = []

        row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"}
        row2 = {"a","s", "d", "f", "g", "h", "j", "k", "l", "A","S", "D", "F", "G", "H", "J", "K", "L"}
        row3 = {"z", "x", "c", "v","b","n","m","Z", "X", "C", "V","B","N","M"}

        for word in words:
            rows = set()
            for c in word:
                if c in row1:
                    rows.add("1")
                elif c in row2:
                    rows.add("2")
                else:
                    rows.add("3")
            if len(rows) == 1:
                res.append(word)

        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna