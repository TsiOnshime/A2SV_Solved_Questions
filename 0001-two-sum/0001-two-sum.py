class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {nums[i]: i for i in range(len(nums))}
        # {2:0, 7:1, 11:2, 15:3}
        # {3:1}
        for i in range(len(nums)): # 0    1
            complement = target - nums[i] # 3
            if complement in hashMap and hashMap[complement] != i:
                return [i,hashMap[complement]]

        return []