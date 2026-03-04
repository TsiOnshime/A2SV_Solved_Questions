from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums, k):

        """
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

nums = [23, 2, 4, 6, 7] k = 6
sum(i, j) = prefix[j] - prefix[i - 1]

sum % k == 0

current = 23 % k = 5
current = 25 % k = 1
current = 29 % k = 5
current = 35 % k = 5
current = 42 % k = 0


{
    5: 0,
    1: 1
    5: 2
}
if we see the same remainder twice that means there is a multiple of 6 between the index we're at and the index the remainder value is at

        """    
        hashmap = {0: -1}
        current = 0
        for i, num in enumerate(nums):
            current += num
            remainder = current % k 
            if remainder not in hashmap:
                hashmap[remainder] = i
            elif i - hashmap[remainder] > 1:
                return True
        return False

# o = Solution()
# print(o.checkSubarraySum([23,2,6,4,7], 13))

                
                

