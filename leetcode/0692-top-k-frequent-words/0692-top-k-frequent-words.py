class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        count_word = defaultdict(list)
        res = []
        min_heap = [] # to store the k highest frequencies

        for word, cnt in word_count.items():
            count_word[cnt].append(word)

        for key in count_word.keys():
            count_word[key].sort()
            heapq.heappush(min_heap, key)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        min_heap = [-i for i in min_heap]
        heapq.heapify(min_heap)

        while min_heap and len(res) < k:
            cnt = heapq.heappop(min_heap)
            for ws in count_word[-cnt]:
                res.append(ws)
                if len(res) == k:
                    break
        return res
            

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna