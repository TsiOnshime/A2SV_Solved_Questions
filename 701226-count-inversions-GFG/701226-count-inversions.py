class Solution:
    def inversionCount(self, arr):
        
        def merge(l, mid, r):
            temp = []
            count = 0
            i = l
            j = mid + 1

            while i <= mid and j <= r:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    count += (mid - i + 1)
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= r:
                temp.append(arr[j])
                j += 1
            for i in range(l, r + 1):
                arr[i] = temp[i - l]

            return count

        def divide(l, r):
            cnt = 0
            if l >= r:
                return 0

            mid = l + (r - l)//2

            cnt += divide(l, mid)
            cnt += divide(mid + 1, r)

            cnt += merge(l, mid, r)
            
            return cnt

        return divide(0, len(arr) - 1)
        





        
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna