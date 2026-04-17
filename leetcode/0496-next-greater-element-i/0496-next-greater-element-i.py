class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = defaultdict(lambda:-1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                elem = stack.pop() 
                hashMap[elem] = num
            stack.append(num)

        return [hashMap[i] for i in nums1]

        

