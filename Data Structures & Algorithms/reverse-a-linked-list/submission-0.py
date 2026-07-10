# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head

        address = None
        while head.next != None:
            temp_next = head.next
            head.next = address
            address = head
            head = temp_next
        head.next = address
        return head