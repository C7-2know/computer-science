# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack=[]
        node=head
        while node:
            stack.append(node)
            node=node.next
        node=head
        half=len(stack)//2+1
        while len(stack)>half:
            ls=stack.pop()
            stack[-1].next=None
            ls.next=node.next
            node.next=ls
            node=ls.next
        return node