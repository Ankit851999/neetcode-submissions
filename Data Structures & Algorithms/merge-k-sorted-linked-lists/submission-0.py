# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n :
            return None
        dummy = ListNode()
        head = dummy
        while True:
            small = -1
            for i in range(n):
                if small == -1:
                     if lists[i]:
                        small = i
                elif lists[i] and lists[i].val < lists[small].val:
                    small = i
            if small == -1:
                break
            new = ListNode(lists[small].val)
            dummy.next = new
            dummy = new
            lists[small] = lists[small].next
            
        return head.next