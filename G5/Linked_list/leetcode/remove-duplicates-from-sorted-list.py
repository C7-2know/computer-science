# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        curr=None
        if prev!=None:
            curr=head.next
        while curr!=None:
            if curr.val!=prev.val:
                prev.next=curr
                prev=curr
                curr=curr.next
                prev.next=None
            else:
                prev.next=None
                curr=curr.next
        return head
