# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        temp = []

        curr = head

        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        c = Counter(temp)

        temp = [k for k, v in c.items() if v == 1]

        dummy = curr = ListNode()

        for i in temp:
            curr.next = ListNode(i)
            curr = curr.next
        
        return dummy.next


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna