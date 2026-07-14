# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_l1 = l1
        temp_l2 = l2
        carry = 0
        dummy = ListNode()
        mainHead = dummy
        while temp_l1 or temp_l2:
            total = (temp_l2.val + temp_l1.val if temp_l2 and temp_l1
            else temp_l2.val if temp_l2  
            else temp_l1.val if temp_l1 
            else 0) + carry
            carry = total // 10
            vaal = total % 10 
            newNode = ListNode(vaal, None)
            dummy.next = newNode
            dummy = newNode
            if temp_l1:
                temp_l1 = temp_l1.next
            if temp_l2:
                temp_l2 = temp_l2.next
        if carry:
            newNode = ListNode(carry, None)
            dummy.next = newNode
        return mainHead.next


