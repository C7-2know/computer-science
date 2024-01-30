# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node=head
        dc=set()
        while curr_node:
            # print(curr_node.val,dc)
            if curr_node in dc:
                return True
            dc.add(curr_node)
            curr_node=curr_node.next
        return False