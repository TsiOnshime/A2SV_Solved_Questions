class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []


        for i in nums:
            answer.extend(list(str(i)))
        return [int(i) for i in answer]


        