# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        main_head = head
        while head and head.next:
            nxt = head.next
            temp = head
            tail = temp
            while temp and temp.next:
                tail = temp
                temp = temp.next
            if tail.next == nxt:
                break
            tail.next = None
            temp.next = nxt
            head.next = temp
            head = nxt
        head = main_head
        return

        

        
