# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        main_head = head
        arr = []
        while head:
            arr.append(head)
            head = head.next
        head = main_head
        if len(arr) < 2:
            return
        right = len(arr) -1
        left = 0
        while right  - left > 1:
            arr[left].next = arr[right]
            arr[right].next = arr[left +1]
            arr[right -1].next = None
            right -= 1
            left += 1
        return



        

        
