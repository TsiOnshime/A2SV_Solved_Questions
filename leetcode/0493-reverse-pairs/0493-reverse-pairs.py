class Solution:
    def reversePairs(self, nums):
        
        self.count = 0
        # [6] [1, 2]
        def divide(l, r):
            if l == r:
                return 
            
            mid = l + (r - l)//2
            divide(l, mid)
            divide(mid + 1, r)
            merge(l, mid, r)

        def merge(l, mid, r):
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > ( 2 * nums[j]):
                    j += 1
                self.count += j - 1 - mid     
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
        return self.count
    
