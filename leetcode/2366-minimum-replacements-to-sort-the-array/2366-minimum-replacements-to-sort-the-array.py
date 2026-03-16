class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # what are we doing?
        # splitting an element in an array till our array is sorted
        # let's start from the last element
        # that would be the max of our array
        # so when we iterate from the last we compare the max element with the element before it if the max element is lesser or our value at the left is greater we split that element
        # how do we split it?
        # we will divide the left / max this tells us how many elements the left elements have to be
        # and our split will be parts - 1
        # then we have to reset our max element because we will use it for the remaining elements at the left side 
        # the max element should be the maximum it could be (we have to maximize it) so our splits will be minimized
        # for eg. (2,5,3) if we check 5 and 3 since 5 is greater it should be parted to ceil(5/ 3) = 2 elements that could be either [1,4], [2,3], [3,2], [4, 1] then we calculate what should be the left most element of the parts by using 5//2 = 2 which means left//parts this tell us [2, 3] is the valid part

        splits = 0
        _max = nums[-1]
        for i in range(len(nums) -1 , -1, -1):
            left = nums[i]
            if left > _max:
                parts = math.ceil(left/_max)
                splits += parts - 1
                _max = (left//parts)
            else:
                _max = left
        return splits