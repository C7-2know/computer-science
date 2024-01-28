# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        size=0
        while curr!=None:
            size+=1
            curr=curr.next
        curr=head
        for i in range(size):
            if i==size//2:
                out=ListNode(curr.val)
                ls=out
            elif i>size//2:
                ls.next=ListNode(curr.val)
                ls=ls.next
            curr=curr.next
        return out
            
