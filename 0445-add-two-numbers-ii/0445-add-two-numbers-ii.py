# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return 
        num1 = 0
        num2 = 0
        dummy = curr = ListNode()
        while l1:
            num1 = 10 * num1 + l1.val
            l1 = l1.next
        while l2:
            num2 = 10 * num2 + l2.val
            l2 = l2.next

        _sum = num1 + num2
        
        if not _sum:
            return ListNode(0)
        curr = None
        while _sum:
            temp = ListNode(_sum % 10, curr)
            curr = temp

            _sum //= 10

        return curr








# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna