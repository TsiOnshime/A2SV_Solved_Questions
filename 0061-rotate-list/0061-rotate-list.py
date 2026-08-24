# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        tail.next =head
        pivot = length - (k % length)

        curr = head
        count = 1
        while count != pivot:
            curr = curr.next
            count += 1
        new_head = curr.next
        curr.next = None
        return new_head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna