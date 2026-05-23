# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = l1
        tail = dummy
        carry = 0

        def calculate_sum_carry(val1, val2, carry):
            _sum = val1 + val2 + carry 
            return [_sum % 10, _sum // 10]
            
        while l1 or l2 or carry:

            if l1 and l2:
                l1.val, carry = calculate_sum_carry(l1.val, l2.val, carry)
                tail = l1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1.val, carry = calculate_sum_carry(l1.val, 0, carry)
                tail = l1
                l1 = l1.next
            elif l2:
                val, carry = calculate_sum_carry(0, l2.val, carry)
                tail.next = ListNode(val)
                tail = tail.next
                l2 = l2.next
            else:
                val, carry = carry, 0
                tail.next = ListNode(val)
                tail = tail.next
        
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna