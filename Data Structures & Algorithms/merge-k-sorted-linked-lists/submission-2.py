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
        from heapq import heappop, heappush

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,((lists[i].val,i,lists[i])))

        dummy = ListNode()
        tail = dummy
        while heap:
            _, i, node = heappop(heap)
            new = ListNode(_)
            dummy.next = new
            dummy = new
            nxt = node.next
            if nxt:
                heappush(heap, (nxt.val,i,nxt))
        return tail.next




