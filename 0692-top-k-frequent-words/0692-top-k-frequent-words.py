class HeapItem:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, to_compare):
        if self.count == to_compare.count:
            return self.word > to_compare.word
        return self.count < to_compare.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        word_freq = Counter(words)
        heap = []
        res = []
        for word, count in word_freq.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if not item < heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)

        while heap:
            res.append(heapq.heappop(heap).word)

        return list(reversed(res))

        










# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna