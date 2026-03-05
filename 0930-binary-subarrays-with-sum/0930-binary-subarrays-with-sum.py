class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # sum(i,j) = prefix[j] - prefix[i - 1]
        # goal = prefix[j] - prefix[i - 1]
        # prefix[j] - goal = prefix[i - 1]
        # The question is have we seen a prefix sum of prefix[i - 1] before if yes count ++
        current_sum = 0
        prefix = []
        for i in range(len(nums)):
            current_sum += nums[i]
            prefix.append(current_sum)
        
        count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        for i in range(len(prefix)):
            diff = prefix[i] - goal
            if prefix_count[diff] != 0:
                count += prefix_count[diff]
            prefix_count[prefix[i]] += 1
        return count
            

