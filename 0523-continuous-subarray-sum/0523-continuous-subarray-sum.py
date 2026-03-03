class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}

        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder_index:
                remainder_index[r] = i
            elif i - remainder_index[r] > 1:
                return True
        return False

                
                

