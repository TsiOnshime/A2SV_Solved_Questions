class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return [keys for keys, values in sorted(count.items(), key = lambda items: items[1], reverse=True)][0]