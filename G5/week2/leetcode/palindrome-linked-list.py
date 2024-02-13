# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        sp=head
        fp=head
        while fp!=None:
            fp=fp.next
            if fp!=None:
                fp=fp.next
            sp=sp.next
        fp=head
        f_half=''
        s_half=''
        while sp!=None:
            f_half+=str(fp.val)
            s_half=str(sp.val)+s_half
            sp=sp.next
            fp=fp.next
        return s_half==f_half
