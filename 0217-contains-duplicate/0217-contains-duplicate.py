class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        print(count)
        for value in count.values():
            print(value)
            return True if value > 1 else False
        