class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def divide(l,r):
            if l == r:
                return 
            mid = l + (r - l)//2
            divide(l, mid)
            divide(mid + 1, r)
            merge(l, mid , r)
        def merge(l, mid, r):
            temp = []
            low = l 
            high = mid + 1
            while low <= mid and high <= r:
                if nums[low] <= nums[high]:
                    temp.append(nums[low])
                    low += 1
                else:
                    temp.append(nums[high])
                    high += 1
            
            temp.extend(nums[low:mid+1])
            temp.extend(nums[high:r+1])

           
            for i in range(l, r+1):
                nums[i] = temp[i - l]
                      
        divide(0, len(nums) - 1)
        return nums
