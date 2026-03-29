class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count = Counter(nums)
        if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:

            if len(count) == 3:
                return "scalene"
            elif len(count) == 1:
                return "equilateral"
            elif len(count) == 2:
                return "isosceles"
        else:
            return "none"