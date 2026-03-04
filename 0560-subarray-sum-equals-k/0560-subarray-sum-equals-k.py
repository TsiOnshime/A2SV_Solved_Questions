class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # sum(i, j) = prefix[j] - prefix[i - 1]
        # k = prefix[j] - prefix[i - 1]
        # prefix[j] - k = prefix[i - 1]
        # so our question is have we seen sum that's equal to prefix[i - 1] before this element
        # we maintain a dic with prefix[i - 1] and count
        # we initialize it to be 0: 1 since when we start the sum is zero and we have seen it once
        # for each element we calculate the running sum
        # we substract k from it and
        # check if dic[prefix[i - 1]] exists if so increment count and the value of dic[prefix[i - 1]] by 1
        # else add dic[prefix[i - 1]] 

        running_sum = 0
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            diff = running_sum - k
            if dic[diff] != 0:
                count += dic[diff]
            dic[running_sum] += 1
        return count
            






