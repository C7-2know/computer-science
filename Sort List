# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 0
        if not head:
            return head

        node = head
        sorted_list = []

        # Step 1: 
        while node:
            sorted_list.append(node.val)
            node = node.next

        # Step 2:
        sorted_list.sort()

        # Step 3: 
        node = head
        for val in sorted_list:
            node.val = val
            node = node.next

        return head
