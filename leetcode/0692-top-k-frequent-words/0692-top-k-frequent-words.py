class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        word_count = Counter(words)
        bucket = [[] for i in range(n + 1)]
        res = []

        for word, freq in word_count.items():
            bucket[freq].append(word)

        for i in range(len(bucket)):
            bucket[i].sort()

        for i in range(n, -1, -1):
            
            for w in bucket[i]:
                res.append(w)
                if len(res) == k:
                    return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna