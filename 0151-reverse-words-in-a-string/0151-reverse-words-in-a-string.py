class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            word = []
            while i >= 0 and s[i] != " ":
                word.append(s[i])
                i -= 1
            l, r = 0, len(word) - 1
            while l <= r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            if word:
                words.append("".join(word))
            i -= 1

        return " ".join(words)


            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna