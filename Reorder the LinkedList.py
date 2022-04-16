# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if slow==fast:
            return
        stack=[]
        p,slow=slow,slow.next
        p.next=None
        while slow:
            stack.append(slow)
            slow=slow.next
        p=head
        while stack:
            top=stack.pop()
            p.next,top.next=top,p.next
            p=top.next
        return head
