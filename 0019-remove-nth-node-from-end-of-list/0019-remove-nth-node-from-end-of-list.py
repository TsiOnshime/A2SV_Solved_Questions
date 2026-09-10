# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        while n and ptr1.next:
            ptr1 = ptr1.next
            n -= 1
        if n:
            return head.next

        while ptr1 and ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return head



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna