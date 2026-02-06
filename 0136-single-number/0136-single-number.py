class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums_to_frequency = {}
        
        # for i in nums:
        #     if i not in nums_to_frequency:
        #         nums_to_frequency[i] = 1
        #     else:
        #         nums_to_frequency[i] += 1

        # for key, value in nums_to_frequency.items():
        #     if value == 1:
        #         return key


        # { 1: (1), 3: (2,3)} frequency: nums

        #########   Even Simpler    ########


        freq = Counter(nums)


        for key, value in freq.items():
            if value == 1:
                return key






        # for i in nums:
        #     count = nums.count(i)
        #     if count == 1:
        #         return i

