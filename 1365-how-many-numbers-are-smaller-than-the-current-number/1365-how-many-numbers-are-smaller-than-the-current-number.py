class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        prefix = [0] * (max(nums) + 1)
        for i in nums:
            prefix[i] += 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        print(prefix)
        res = [0] * len(nums)
        for i in range(len(res)):
            num = nums[i]
            smaller = (prefix[num - 1]) if num > 0 else 0
            res[i] = smaller
        return res

 
