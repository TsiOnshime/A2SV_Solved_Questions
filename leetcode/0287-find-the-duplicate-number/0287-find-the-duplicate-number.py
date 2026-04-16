class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ### FLOYD's time to shine

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow

            

            