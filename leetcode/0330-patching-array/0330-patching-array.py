class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        _range = [0, 0]
        i = 0
        patch = 0
        length = len(nums)
        while _range[1] < n:
            if i < length and _range[1] + 1 >= nums[i]:
                _range[1] += nums[i]
                i += 1
            else:
                _range[1] += (_range[1] + 1)
                patch += 1
        return patch

