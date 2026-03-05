class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0 # degree of an array
        count = {} # count the number of times a number appears (frequency of each number)
        first_seen = {} # holds the first occurence index of each number in nums
        min_length = 0 # holds the minimum length of a subarray which has a degree of degree

        for i in range(len(nums)):
            if nums[i] not in first_seen:
                first_seen[nums[i]] = i
            count[nums[i]] = count.get(nums[i], 0) + 1 # to store the freq of each number in nums
            if count[nums[i]] > degree: # if the freq of num is greater than our degree
                degree = count[nums[i]] # we reset the degree to be the freq of the current element
                min_length = i - first_seen[nums[i]] + 1
            elif count[nums[i]] == degree: # this works when we have more than one element with degree d 
                min_length = min(min_length, i - first_seen[nums[i]] + 1)
            
        return min_length



        

        """
        count           first_seen          degree          min_length
        {}                  {}                 0                0
        {1:1}              {1:0}  
      {1: 1, 2: 1}        {1: 0, 2: 1}             
    {1:1, 2:2}
        """





