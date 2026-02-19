class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)


        int_idx = {}

        for i in sorted_nums:
            if i not in int_idx:
                int_idx[i] = sorted_nums.index(i)
   

        for i in nums:
            score = int_idx[i]
            res.append(score)

        return res




            