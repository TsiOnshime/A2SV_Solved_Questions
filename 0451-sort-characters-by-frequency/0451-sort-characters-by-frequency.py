class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) # char -> cnt
        buckets = defaultdict(list) # freq -> [char]


        for char, cnt in count.items():
            buckets[cnt].append(char)

        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)

        return "".join(res)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna