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
        word_count = Counter(words)
        heap = []
        res = []
        for word, cnt in word_count.items():
            item = HeapItem(word, cnt)
            if len(heap) < k:
                heapq.heappush(heap,item)
            else:
                if not item < heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)

        while k:
            item = heapq.heappop(heap)
            res.append(item.word)
            k -= 1

        res = list(reversed(res))
        return res


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna