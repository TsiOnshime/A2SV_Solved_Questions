class Wrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, to_compare):
        return self.node.val < to_compare.node.val
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, Wrapper(node))

        dummy = tail = ListNode()

        while min_heap:
            smallest = heapq.heappop(min_heap).node
            tail.next = smallest
            tail = tail.next
            nxt = smallest.next
            if nxt:
                heapq.heappush(min_heap, Wrapper(nxt))

        return dummy.next

        

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna