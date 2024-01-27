# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=None
        out=None
        fs=out
        if head!=None:
            out=ListNode(head.val)
            curr=head.next
            fs=out
        while curr!=None:
            new=ListNode(curr.val)
            new.next=fs
            fs=new
            curr=curr.next
            
        return fs
