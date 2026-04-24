class Solution:
    def inversionCount(self, arr):
        # Code Here
        self.count = 0
        def divide(l, r):
            if l == r:
                return
            mid = l + (r - l)//2
            divide(l, mid)
            divide(mid + 1, r)
            merge(l, mid, r)
            
        def merge(l, mid, r):
            temp = []
            low = l
            high = mid + 1
            
            while low <= mid and high <= r:
                if arr[low] <= arr[high]:
                    temp.append(arr[low])
                    low += 1
                else:
                    self.count += (mid - low + 1)
                    temp.append(arr[high])
                    high += 1
                    
            temp.extend(arr[low:mid + 1])
            temp.extend(arr[high:r + 1])
            
            for i in range(l, r + 1):
                arr[i] = temp[i - l]
            
        divide(0, len(arr) - 1)
        return self.count