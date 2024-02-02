# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node=head
        if curr_node!=None:
            last_node=head.next
        else:
            return head
        sec=last_node
        
        while curr_node.next!=None and last_node.next!=None:
            curr_node.next=last_node.next
            curr_node=curr_node.next
            if curr_node!=None:
                last_node.next=curr_node.next
                last_node=last_node.next
        curr_node.next=sec
        return(head)