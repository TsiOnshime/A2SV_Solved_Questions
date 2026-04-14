# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        index = 0
        while curr:
         
            if isinstance(curr.val, list):
                return True
            else:
                curr.val = [index, curr.val]
            curr = curr.next
            index += 1

        return False