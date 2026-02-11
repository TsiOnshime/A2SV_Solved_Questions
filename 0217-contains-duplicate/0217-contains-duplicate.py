class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums)

        if len(sett) < len(nums):
            return True
        return False
        