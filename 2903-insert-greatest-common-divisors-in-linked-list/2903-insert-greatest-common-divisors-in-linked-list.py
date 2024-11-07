# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            a,b=min(a,b),max(a,b)
            while b>0:
                t=b
                b=a%b
                a=t
            return a 
        cur=head
        prev=head
        while prev.next:
            cur=prev.next.val
            gc=gcd(prev.val,cur)
            new=ListNode(gc)
            new.next=prev.next
            prev.next=new
            prev=new.next
        return head   