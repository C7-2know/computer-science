# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode()
        lnode=less
        great=ListNode()
        gl_node=great
        curr=head
        while curr:
            if curr.val<x:
                lnode.next=curr
                lnode=curr
            else:
                gl_node.next=curr
                gl_node=curr
            curr=curr.next
        if less.next==None:
            return great.next
        elif great.next==None:
            return less.next
        lnode.next=great.next
        gl_node.next=None
        return less.next