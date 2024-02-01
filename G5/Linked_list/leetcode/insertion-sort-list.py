# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        prev = dummy 
        current = head
        
        while current:
            if current.next and current.next.val < current.val:
                while prev.next and prev.next.val < current.next.val:
                    prev = prev.next
                temp = prev.next
                prev.next = current.next
                current.next = current.next.next
                prev.next.next = temp
                prev = dummy
            else:
                current = current.next
        return dummy.next       