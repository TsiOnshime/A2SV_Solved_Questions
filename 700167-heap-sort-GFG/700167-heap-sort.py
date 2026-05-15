class Solution:
    def heapSort(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.heapify_down(arr, n, i)

        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify_down(arr, i, 0)
        
        return arr
            
    def heapify_down(self,arr, n, i):
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest == i:
                break
            arr[largest], arr[i] = arr[i], arr[largest]
            i = largest
    
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna