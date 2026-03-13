class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
# what we will do is be greedy think about the first element only the other two don't worry about them
# we will iterate till the last two elements because we have to have three elements that have to be flipped
# use a helper function to flip
# [1,0,0,1,1,0,1,1,1] => [1,0,0,1,1,0,1,1,1] => [1,1,1,0,1,0,1,1,1] => [1,1,1,0,1,0,1,1,1] => [1,1,1,1,0,1,1,1,1] => [1,1,1,1,1,0,0,1,1] => [1,1,1,1,1,1,1,0,1]
        def flip(number):
            return 0 if number else 1
        min_flip = 0
        for i in range(len(nums) -2):
            if nums[i] == 0:
                nums[i] = flip(nums[i])
                nums[i + 1] = flip(nums[i + 1])
                nums[i + 2] = flip(nums[i + 2])
                min_flip += 1
    
        if not nums[-1] or not nums[-2]:
            return -1
        return min_flip
