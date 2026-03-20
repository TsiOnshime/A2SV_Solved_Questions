class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# 9 - 2 = 7 
# 9 - 7 = 2
# 9 - 11 = -2

        hashmap = {nums[i]: i for i in range(len(nums))}
        print(hashmap)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]
                
            

