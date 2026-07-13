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
        dummy = Node(0)
        NewList = dummy
        mainHead = head
        maap = {}
        while head:
            new = Node(head.val, None,None)
            maap[head] = new
            dummy.next = new
            head = head.next
            dummy = dummy.next
        head = mainHead
        dummy = NewList.next
        while head:
            dummy.random = maap[head.random] if head.random != None else None
            head = head.next
            dummy = dummy.next

        return NewList.next

        
