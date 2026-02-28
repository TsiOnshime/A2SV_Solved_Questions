class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # We will use a sliding window
        # l = 0 , 
        # res = 0
        # count = defaultdict(int)
        # we will iterate r = 0 -- n -1
        # we add count[nums[r]] += 1
        # zero_count = count[nums[0]]
        # while zero_count > 1:
        # count[nums[l]] -= 1
        # if count[nums[l]] <= 0:
        # del count[nums[l]]
        # zero_count = count[nums[0]]
        # l += 1
        # res = max(res,r - l + 1)
        n = len(nums)
        l = 0
        res = 0
        count = defaultdict(int)
        for r in range(n):
            count[nums[r]] += 1
            zero_count = count[0]
            while zero_count > 1:
                count[nums[l]] -= 1
                if count[nums[l]] <= 0:
                    del count[nums[l]]
                zero_count = count[0]
                l += 1
            res = max(res, r - l + 1)

        return res - 1
