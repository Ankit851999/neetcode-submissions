# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        head1 = head
        head2 = head
        while head2 and head2.next and head2.next.next:
            head1 = head1.next
            head2 = head2.next.next
        
        mid = head1
        head1 = head1.next
        prev = None
        while head1:
            nxt = head1.next
            head1.next = prev
            prev = head1
            head1 = nxt
        mid.next = None
        head1 = head
        head2 = prev

        while head1 and head2:
            nxt = head1.next
            nxt2 = head2.next
            head1.next = head2
            head2.next = nxt
            head2 = nxt2
            head1 =nxt
        return


