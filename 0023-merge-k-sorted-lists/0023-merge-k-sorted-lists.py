# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        l1 = lists[0]
        l2 = lists[1]

        def divide(l, r):  
            if l > r:
                return     # 0, 2      # 0, 1     merge(0, 1)  #2,2
            if l == r:
                return lists[l]
            mid = l + (r - l) // 2

            left = divide(l, mid)
            right = divide(mid + 1, r)
            return merge(left, right)
        

        def merge(l1, l2):
            

            dummy = tail = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
            
    

        return divide(0, len(lists) - 1)