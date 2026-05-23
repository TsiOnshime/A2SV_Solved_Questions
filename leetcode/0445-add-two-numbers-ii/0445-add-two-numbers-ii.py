# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        carry = 0
        dummy = ListNode()
       

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next


        print(stack1)
        print(stack2)

        # [7, 2, 4, 3]
        #    [5, 6, 4]
        # val1 = 7               val2 = 0
        # _sum = 7
        # val = 7      carry = 0
        # dummy -> | 7 | -> | 8 | -> | 0 | -> | 7 | -> None
        #  

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            _sum = val1 + val2 + carry
            val = _sum % 10
            carry = _sum // 10
            
            curr = ListNode(val)

            curr.next = dummy.next
            dummy.next = curr

        return dummy.next





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna