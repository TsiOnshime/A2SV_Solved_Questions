class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # a + b > c 
        # a + c > b
        # b + c > a
        perimeter = 0
       

        nums.sort(reverse=True)
        i = 0
        while i + 2 < len(nums):
            
            if nums[i] < nums[i + 1] + nums[i + 2]:
                perimeter = max(perimeter, nums[i] + nums[i + 1] + nums[i + 2])
            i += 1
        
                







        return perimeter

