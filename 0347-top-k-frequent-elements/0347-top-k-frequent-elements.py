class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []

        count = Counter(nums)

        return list(count.keys())[0:k]
            