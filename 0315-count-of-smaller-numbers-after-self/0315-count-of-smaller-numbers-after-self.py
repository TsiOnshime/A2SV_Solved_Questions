class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        numsPair = []
        for i, val in enumerate(nums):
            numsPair.append([i, val])

        def divide(l, r):
            if l == r:return 
            mid = l + (r - l)//2
            divide(l, mid)
            divide(mid + 1, r)
            merge(l, mid, r)

        def merge(l, mid, r):
            nonlocal ans

            temp = []
            low = l
            high = mid + 1
            while low <= mid and high <= r:
                if numsPair[low][1] > numsPair[high][1]:
                    temp.append(numsPair[low])
                    ans[numsPair[low][0]] += r - high + 1
                    low += 1
                else:
                    temp.append(numsPair[high])
                    high += 1
            temp.extend(numsPair[low:mid+1])
            temp.extend(numsPair[high:r+1])
            for i in range(l, r+1):
                numsPair[i] = temp[i - l]
        divide(0, len(nums) - 1)
        return ans

