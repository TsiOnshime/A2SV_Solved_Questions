class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #  nums = [2,0,2,1,1,0]
        k = max(nums)
        counts = [0] * (k + 1)
        
        for num in nums:
            counts[num] += 1
            
        # counts = [2, 2, 2]
        
        starting_index = 0
        
        for i, count in enumerate(counts): # 0 2    1, 2    2 2
            counts[i] = starting_index # [0]       [0,2]    [0,2,4]
            starting_index += count # 2     4       6
        
        sorted_nums = [0] * len(nums)
        
        for elem in nums:
            sorted_nums[counts[elem]] = elem
            
            counts[elem] += 1
            
        for i in range(len(sorted_nums)):
            nums[i] = sorted_nums[i]
            
        return nums
        
            
            
        