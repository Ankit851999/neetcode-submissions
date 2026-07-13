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
        if not head:
            return None
        cur_head = head
        while head:
            new = Node(head.val,head.next)      
            head.next = new
            head = new.next
        head = cur_head
        while head:
            head.next.random = head.random.next if head.random != None else None
            head = head.next.next
        
        head = cur_head
        copy_head = head.next
        copy = copy_head
        while head:
            head.next = head.next.next
            if copy.next:
                copy.next = copy.next.next
                copy = copy.next
            head= head.next

        return copy_head

            
