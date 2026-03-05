# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        node=head
        while True:
            cur=ListNode(float('inf'))
            ind=0
            for i in range(len(lists)):
                if lists[i] and lists[i].val<cur.val:
                    cur=lists[i]
                    ind=i
            if cur.val<float('inf'):
                if not head:
                    head=ListNode(cur.val)
                    node=head
                else:
                    node.next=ListNode(cur.val)
                    node=node.next
                lists[ind]=lists[ind].next
            else:
                return head
                