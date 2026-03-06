class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        freq = [0] * len(nums)
        freq.append(float('-inf'))
        for request in requests:
            freq[request[0]] += 1
            freq[request[1] + 1] -= 1
        
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        temp = freq
        nums.sort(reverse=True)
        freq.sort(reverse=True)
    
        print(f"{nums=}")
        print(f"{freq=}")
        _sum = 0
      
        for i in range(len(nums)):
            _sum += (nums[i] * freq[i])
        return _sum % (10**9 + 7)
        