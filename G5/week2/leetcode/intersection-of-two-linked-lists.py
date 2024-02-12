# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr=headA
        nA=0
        while curr!=None:
            nA+=1
            curr=curr.next
        curr=headB
        nB=0
        while curr!=None:
            nB+=1
            curr=curr.next
        curr=headA
        curr2=headB
        if nB>nA:
            curr=headB
            curr2=headA
        for _ in range(abs(nA-nB)):
            curr=curr.next
        while curr!=None:
            if curr==curr2:
                return curr
            curr=curr.next
            curr2=curr2.next
        return None