# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur1=l1
        while cur1:
            stack.append(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        stack2 = []
        while cur2:
            stack2.append(cur2.val) 
            cur2 = cur2.next
        ans = []
        r = 0
        while stack and stack2:
            v1, v2 = stack.pop(), stack2.pop()
            sum_ = v1+v2+r
            r= sum_//10
            ans.append(sum_%10)
        while stack:
            v1 = stack.pop()
            sum_ = v1+r
            r= sum_//10
            ans.append(sum_%10)
        while stack2:
            v1 = stack2.pop()
            sum_ = v1+r
            r= sum_//10
            ans.append(sum_%10)
        if r>=1:
            ans.append(r)
        result = ListNode(ans.pop())
        cur = result
        while ans:
            i = ans.pop()
            cur.next = ListNode(i)
            cur = cur.next
        return result