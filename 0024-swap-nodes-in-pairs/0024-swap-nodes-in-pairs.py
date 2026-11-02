# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        def swap(curr_node, nxt_node):
            nxt = nxt_node.next
            curr_node.next = nxt
            nxt_node.next = curr_node
            return nxt_node
        
        while curr and curr.next:
            prev.next = swap(curr, curr.next)
            prev = curr
            curr = curr.next
        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna