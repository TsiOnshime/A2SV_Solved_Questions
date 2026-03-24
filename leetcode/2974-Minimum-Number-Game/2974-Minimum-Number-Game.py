class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        bob = False

        while nums:
            Amin = min(nums)
            nums.remove(min(nums))
            if nums:
                Bmin = min(nums)
                nums.remove(min(nums))
                bob = True
            if bob:
                arr.append(Bmin)
            arr.append(Amin)
        return arr