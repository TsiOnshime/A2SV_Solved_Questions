class Solution:
    def inversionCount(self, arr):
        # Code Here
        count = 0
        def merge(l, mid, r):
            
            first = l 
            second = mid + 1
            temp = []
            cnt = 0
            while first <= mid and second <= r:
                if arr[first] <= arr[second]:
                    temp.append(arr[first])
                    first += 1
                else:
                    cnt += mid - first + 1
                    temp.append(arr[second])
                    second += 1
            while first <= mid:
                temp.append(arr[first])
                first += 1

            while second <= r:
                temp.append(arr[second])
                second += 1   
            for i in range(l, r + 1):
                arr[i] = temp[i - l]
            return cnt
            
            
        def divide(l, r):
            nonlocal count
            if l >= r:
                return 
            mid = l + (r - l)//2
            
            divide(l,mid)
            divide(mid + 1, r)
            
            count += merge(l, mid, r)
        divide(0, len(arr) - 1) 
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna