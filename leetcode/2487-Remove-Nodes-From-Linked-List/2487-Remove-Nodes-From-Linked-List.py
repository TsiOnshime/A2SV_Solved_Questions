# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = ListNode(head.val)
        start = stack
        
        current = head.next
        while current:
            while start and start.val < current.val:
                start = start.next
            add = ListNode(current.val)
            add.next = start
            start = add 
            current = current.next
        
        _prev = None
        _current = start
        _next = start.next

        while _current:
            _current.next = _prev
            _prev = _current 
            _current = _next
            if _next:
                _next = _next.next
        return _prev