class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # sliding window using three pointers
        # use three pointers left_far, left_near, right 
        # initialize the lefts to zer0
        # initialize a count dic
        # insert the first element of nums and 1 as its value
        # for r 1...n-1
        # add the value of nums[r] into our count
        # in a while loop condition: check if we have excess of nums[near]
        # if so increment near by 1
        # in another while loop condition: check if len(count) > k:
        # if so near += 1
        # far = near
        # outside of the loops
        # res += far - near
    
        res = 0
        left_far = left_near = 0
        count = defaultdict(int)
        

        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[left_near]] -= 1
                if count[nums[left_near]] <= 0:
                    del count[nums[left_near]]
                left_near += 1
                left_far = left_near
            while count[nums[left_near]] > 1:
                count[nums[left_near]] -= 1
                left_near += 1

            if len(count) == k:
                res += left_near - left_far + 1
        return res
    


     
