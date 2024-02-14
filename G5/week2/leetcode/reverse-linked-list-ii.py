# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        reverse=ListNode()
        rev_end=None
        left_n=None
        n=0
        while curr!=None:
            if n+1==left:
                left_n=curr
            if n>=left and n<=right:
                if n==left:
                    rev_end=curr
                temp=curr.next
                curr.next=reverse.next
                reverse.next=curr
                curr=temp
            else:
                curr=curr.next
            n+=1
            if n>right:
                left_n.next=reverse.next
                rev_end.next=curr
                break
        return dummy.next

