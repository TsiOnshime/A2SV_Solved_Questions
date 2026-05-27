# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even = head.next
        temp1 = even
        temp2 = head
# temp1 = 2 -> None temp2 = 1 -> 3

        while temp1.next and temp2.next:
            if temp1.next:
                temp2.next = temp1.next
                temp2 = temp2.next
                temp1.next = None
            if temp2.next:
                temp1.next = temp2.next
                temp1 = temp1.next


        temp2.next = even
        return head



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna