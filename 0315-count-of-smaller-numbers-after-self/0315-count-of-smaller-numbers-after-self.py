class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sort = []
        def binarySearch(sort, num):
            l = 0
            r = len(sort) - 1
            ans = l
            while l <= r:
                mid = l + (r - l)//2
                if sort[mid] >= num:
                    r = mid - 1
                else:
                    l = mid + 1
            
            sort.insert(l, num)
            
            return l

        for i in range(len(nums) - 1, -1, -1):
            rank = binarySearch(sort, nums[i])
            res[i] = rank
        
    
        return res

