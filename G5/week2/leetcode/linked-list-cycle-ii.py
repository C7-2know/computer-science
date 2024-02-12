# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        p2=False
        pos=0
        while fast and fast.next != None:
            if p2 and slow==fast:
                return slow
            if not p2:
                fast=fast.next.next
            else:
                fast=fast.next
            slow=slow.next
            if slow==fast:
                if p2==True:
                    return slow
                slow=head
                p2=True
        if not p2:
            return None
        