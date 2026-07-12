# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        left = head
        right = head.next

        l = 2

        while right and right.next:
            left = left.next 
            right = right.next.next
            l += 2
        
        if right == None:
            l -= 1

        left_i = l //2
        index = (l - n)
        left = head
        prev = None
        while index:
            prev = left
            left = left.next
            index -= 1
        
        nxt = left.next
        if prev == None:
            return nxt
        prev.next = nxt

        return head

        
        

