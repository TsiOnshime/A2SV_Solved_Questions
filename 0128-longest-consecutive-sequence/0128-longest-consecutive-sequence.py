class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
     
        max_length = 0
       

        for num in set_nums:
            #check if it is the start of a sequence
            if (num -1) not in set_nums:
                length = 1
                while (num + length ) in set_nums:
                    length += 1
                max_length = max(length, max_length)
        return max_length
            
