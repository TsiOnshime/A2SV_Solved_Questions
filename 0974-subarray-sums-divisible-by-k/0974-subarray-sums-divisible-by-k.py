class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # remainder: count
        count = defaultdict(int)
        count[0] = 1

        for i in range(1, len(nums)):
            nums[i] += nums[i -1]

        result = 0
        for i in range(len(nums)):
            remainder = nums[i] % k
            result += count[remainder] 
            count[remainder] += 1
        return result