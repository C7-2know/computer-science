# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        size=0
        while curr!=None:
            size+=1
            curr=curr.next
        curr=head
        part_s=size//k
        rem=size%k
        off=1
        out=[]
        for i in range(k):
            if rem<=0:
                off=0
            rem-=1
            List=ListNode()
            last=List
            for _ in range(part_s+off):
                temp=curr
                if curr!=None:
                    temp=curr.next
                curr.next=None
                last.next=curr
                last=curr
                curr=temp
            out.append(List.next)
        return out
