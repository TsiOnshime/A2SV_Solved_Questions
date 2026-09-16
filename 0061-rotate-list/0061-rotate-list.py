# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        def findNthNode(temp, k):
            cnt = 1
            while temp:
                if cnt == k:
                    return temp
                cnt += 1
                temp = temp.next
            return temp
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        if k == 0:
            return head
        
        if (k % n == 0):
            return head

        k = k % n

        tail.next = head
        newLastNode = findNthNode(head, n - k)

        head = newLastNode.next
        newLastNode.next = None

        return head










# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna