class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) -1 
        per = []
        while i >= 2:
            if nums[i] < nums[i-1] + nums[i-2]:
                per.extend([nums[i], nums[i-1], nums[i-2]])
                break
            i -= 1
        _sum = 0
        for i in per:
            _sum += i

        return _sum

