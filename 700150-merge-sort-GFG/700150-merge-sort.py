class Solution:
    def sort(self,left, right):
            sorted_list = []
            l = 0
            r = 0
            
            while l < len(left) and r < len(right):
                
                if left[l] <= right[r]:
                    sorted_list.append(left[l])
                    l += 1
                else:
                    sorted_list.append(right[r])
                    r += 1
            sorted_list.extend(left[l:])
            sorted_list.extend(right[r:])
            return sorted_list
                
 
    def mergeSort(self, arr, l, r):
        #code here
        if l == r:
            return [arr[l]]
            
        mid = (l + r) // 2
        
        left = self.mergeSort(arr, l, mid)
        right = self.mergeSort(arr, mid+1, r)
        
        merged = self.sort(left, right)
        
        for i in range(len(merged)):
            arr[l + i] = merged[i]
        return merged
        
        
        

                    