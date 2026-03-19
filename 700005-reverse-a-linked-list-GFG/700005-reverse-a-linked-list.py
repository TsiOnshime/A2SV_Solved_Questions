"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # # Code here
        # if head == None or head.next == None:
        #     return head
        
        # def reverse(prev, curr):
            
        #     if not curr:
        #         return prev
                
        #     nxt = curr.next
        #     curr.next = prev
        #     return reverse(curr, nxt)


                
        
        
        
        
        # return reverse(None, head)
        if not head or not head.next:
            return head
            
        curr = head
        prev = None
        nxt = curr.next
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev