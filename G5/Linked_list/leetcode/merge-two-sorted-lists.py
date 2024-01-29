# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1!=None and list2!=None:
            if list1.val<list2.val:
                curr=list1
                head=list1
                sec=list2
            else:
                curr=list2
                head=list2
                sec=list1
        else:
            if list1!=None:
                return list1
            else:
                return list2
        prev=head
        curr=curr.next
        while curr!=None and sec!=None:
            if curr.val<=sec.val:
                prev=curr
                curr=curr.next
            else:
                temp=sec.next
                prev.next=sec
                prev=prev.next
                prev.next=curr
                sec=temp
                # print(curr.val,prev.val)
        if sec!=None:
            prev.next=sec
        else:
            prev.next=curr
        return head

