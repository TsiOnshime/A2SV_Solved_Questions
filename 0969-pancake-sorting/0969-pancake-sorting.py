class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        n = len(arr)
        count = 0
        it will find the maximum element
        i = 3 => arr.index(_max)
        we flip it at arr.index(_max)
        arr[:i] = reverse(arr[:i])
        and append(i + 1)
        [4]
        [4,2,3,1]
        flip at n - count - 1:
        [1,3,2,4]
        append(n - count)
        count += 1
        '''
        # i = 0 
        # _max= max(n[:len(n)- i])

        # [3, 2, 4, 1]        => [] count = 0
        # [4, 2, 3, 1]        => [3] count = 1
        # [1, 3, 2, 4]        => [3, 4] count = 2
        #                                count = 0
        # [1, 3, 2, 4]        =>  [3, 4] count = 0
        # [3, 1, 2, 4]        => [3, 4, 2] count = 1
        # [2, 1 , 3, 4]       => [3, 4, 2, 3] count = 2
        # []
        if arr == sorted(arr):
            return []

        n = len(arr)
        i = 0
        result = []
        while  i < n:
            _max = max(arr[:n-i])
            idx = arr.index(_max)

            arr[:idx+1] = reversed(arr[:idx+1])
           
            result.append(idx+1)


            arr[:n-i] = reversed(arr[:n-i])
            
            result.append(n-i)
 