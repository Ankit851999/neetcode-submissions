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
        dummy = Node(0,head, None)
        mainHead = dummy

        while dummy.next:
            dummy = dummy.next
            new = Node(dummy.val,dummy.next)      
            dummy.next = new
            dummy = new
        dummy = mainHead
        while dummy.next:
            dummy = dummy.next
            dummy.next.random = dummy.random.next if dummy.random else None
            dummy = dummy.next
        dummy = mainHead
        while dummy.next:
            head = dummy.next
            dummy.next = dummy.next.next
            dummy = dummy.next
            head.next = dummy.next
            head = head.next

        return mainHead.next

            
