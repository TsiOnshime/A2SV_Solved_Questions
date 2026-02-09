class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for val in nums:
            dic[val] = target - val
            if dic[val] == val and nums.count(val) == 1:
                continue
            elif dic[val] in nums:
                if dic[val] == val:
                    first = nums.index(val)
                    nums.remove(val)
                    second = nums.index(dic[val]) + 1
                    return[first, second]
                return[nums.index(val), nums.index(dic[val])]
        
        
        