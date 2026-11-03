# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        def reverse(curr, length):
            prev = None
            tail = curr
            after = None

            while length <= right:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                length += 1
            tail.next = curr
            return prev
        
        if left == 1:
            return reverse(head, left)
        
        curr = head
        n = 1

        while n < left - 1:
            curr = curr.next
            n += 1
        
        curr.next = reverse(curr.next, left)
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna