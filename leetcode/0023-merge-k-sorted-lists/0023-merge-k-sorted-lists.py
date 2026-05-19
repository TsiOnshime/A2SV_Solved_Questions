# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = curr = ListNode()
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, [lists[i].val, i, lists[i]])

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            curr.next = node
            curr = node
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(min_heap, [lists[idx].val, idx, lists[idx]])

        return dummy.next

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna