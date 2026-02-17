class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        # n = len(nums)
        # freq = Counter(nums)
        # maxx = 0
        # for key, value in freq.items():
        #     if value > maxx:
        #         maxx = value
        #         dominant = key
        
        # for i in range(n):
        #     left = nums[0:i+1]
        #     len_left = len(left)

        #     right = nums[i+1:n]
        #     len_right = len(right)

            
        #     left_counter = Counter(left)
        #     right_counter = Counter(right)
         

        #     if dominant in left_counter and dominant in right_counter:
        #         if left_counter[dominant] > len_left//2 and right_counter[dominant] > len_right//2:
                   
        #             return i

        # return -1

        n = len(nums)
        freq = Counter(nums)
        m= max(freq.keys(), key = lambda k: freq[k])

        total_count = freq[m]

        count_so_far = 0

        for i in range(n):

            if nums[i] == m:
                count_so_far += 1

            len_left = i + 1
            len_right = n - len_left

            if count_so_far > len_left//2 and (total_count - count_so_far) > len_right//2:
                return i
        return -1
        