class Solution:
    def frequencySort(self, s: str) -> str:
        # ascii values
        # upper case = A - Z = 65 - 90
        # lower case = a - z = 97 - 122
        #  digits = 0 - 9 = 48 - 57

        counts = [[0, 0] for i in range(125)]
        n = len(s)
        for i in range(n):
            idx = ord(s[i])
            counts[idx][0] += 1
            counts[idx][1] = i

        res = []
        counts.sort(key=lambda x: x[0], reverse=True)
       
        for i in range(len(counts)):
            if counts[i][0] == 0:
                break
            freq, letter = counts[i]
            letter = s[letter]
            res.append(letter * freq)

        res = "".join(res)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna