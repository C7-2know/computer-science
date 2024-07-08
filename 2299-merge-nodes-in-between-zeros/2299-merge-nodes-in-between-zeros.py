# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        res=ListNode()
        temp=res
        cur=cur.next
        while cur:
            while cur and cur.val!=0:
                temp.val+=cur.val
                cur=cur.next
            tmp=ListNode()
            cur=cur.next
            if cur:
                temp.next=tmp
                temp=tmp
        temp=None
        return res

            


