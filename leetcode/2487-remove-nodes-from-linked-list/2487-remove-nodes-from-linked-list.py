# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            curr = head
            next = curr.next

            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp

            return prev
        
        head = reverse(head)

        curr = head
        curr_max = head.val

        while curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                curr_max = curr.val



        return reverse(head)

        