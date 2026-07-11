# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        isCycle = False
        head1 = head
        head2 = head
        while head2 and head1:
            head1 = head1.next
            if head2 and head2.next:
                head2 = head2.next.next
            else:
                break
            if head1 == head2:
                return True
        return isCycle

        