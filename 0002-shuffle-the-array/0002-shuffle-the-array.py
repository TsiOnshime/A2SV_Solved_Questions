class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1 = 0
        p2 = n

        new_nums = []
        for i in range(n):
            new_nums.append(nums[p1])
            new_nums.append(nums[p2])
            p1 += 1
            p2 += 1
        return new_nums

