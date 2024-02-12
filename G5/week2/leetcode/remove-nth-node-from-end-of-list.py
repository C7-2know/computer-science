# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr=head
        # ln=0
        # while curr!=None:
        #     ln+=1
        #     curr=curr.next
        # if n<ln:
        #     curr=head
        #     for _ in range(1,ln-n-1):
        #         curr=curr.next
        #     curr.next=curr.next.next
        # return head

        sp=None
        fp=head
        gap=1
        while fp!=None:
            fp=fp.next
            gap+=1
            if gap>n+1:
                if sp==None:
                    sp=head
                else:
                    sp=sp.next
        if sp and sp.next!=None:
            sp.next=sp.next.next
            return head
        elif sp==None and gap==n+1:
            return head.next
        else:
            return sp
        