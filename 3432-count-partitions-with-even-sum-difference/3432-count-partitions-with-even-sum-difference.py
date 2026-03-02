class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        current = 0
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            current += nums[i]
            prefix[i] = current
        print(prefix)

        count = 0
        i = 0
        for i in range(len(prefix)-1):
            _sum_left = prefix[i]
            
            
            _sum_right = prefix[len(nums) - 1] - prefix[i]

            _sum = _sum_left - _sum_right

            if _sum % 2 == 0:
                count += 1
        if count == 0: 
            return 0
        return count - 1
