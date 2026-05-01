class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # pigeon hole Principle
        if len(nums) < 2: return 0
        _max, _min = max(nums), min(nums)
        n = len(nums)
        bucketSize = max(1, (_max - _min) // (n - 1) )
        # 9 - 1 // 3 = 2
        # [1 - 3), [3 - 5), [5 - 7), [7, 9]
        bucket = defaultdict(list)
        for num in nums:
            
            key = (num - _min) // bucketSize
            if key not in bucket:
                bucket[key] = [num, num]
            else:
                bucket[key] = [min(num, bucket[key][0]), max(num, bucket[key][1])]

        
        ans = 0
        prev = -1
        for key in sorted(bucket):
            if prev != -1:
                ans = max(bucket[key][0] - bucket[prev][1], ans)
            prev = key

        return ans