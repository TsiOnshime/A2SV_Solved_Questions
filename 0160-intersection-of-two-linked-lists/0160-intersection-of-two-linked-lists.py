# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        currA, currB = headA, headB
        m, n = 0, 0

        while currA:
            m += 1
            currA = currA.next
        
        while currB:
            n += 1
            currB = currB.next
        
        currA, currB = headA, headB
        if m > n:
            currB, currA = currA, currB
        
        diff = abs(m - n)
        while diff:
            currB = currB.next
            diff -= 1
        
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna