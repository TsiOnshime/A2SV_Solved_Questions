"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None: None}
        # old node : new node

        curr = head
        while curr:
            new_node = Node(curr.val)
            mapping[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            copy = mapping[curr]
            copy.next = mapping[curr.next]
            copy.random = mapping[curr.random]

            curr = curr.next
        return mapping[head]
        