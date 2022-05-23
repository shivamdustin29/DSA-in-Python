# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in lists:
            while i:
                heapq.heappush(res, i.val)
                i = i.next
        
        dummyHead = ListNode(-1)
        tempt = dummyHead
        
        while res:
            newNode = ListNode(heapq.heappop(res))
            tempt.next = newNode
            tempt = tempt.next
        
        return dummyHead.next
        
