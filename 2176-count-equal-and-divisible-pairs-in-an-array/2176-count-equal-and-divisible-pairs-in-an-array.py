class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        
        dic = {}
        for i, num in enumerate(nums):
            dic.setdefault(num, []).append(i)




        count = 0
        for key, value in dic.items():
            if len(dic[key]) == 1:
                continue
            for i in range(len(dic[key]) - 1):
                j = i + 1
                while j < len(dic[key]):
                    if (value[i] * value[j]) % k == 0:
                        count += 1
                        j += 1
                        continue
                    if j == len(dic[key]) - 1 & i != len(dic[key]) - 2:
                        break
                    j += 1
        return count


        # count = 0

        # for i in range(len(nums)):
            
        #     for j in range(i + 1, len(nums)):

        #         if nums[i] == nums[j] and (i * j) % k == 0:
        #             count += 1
        #         continue

        # return count
