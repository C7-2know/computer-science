# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        isSub=False
        memo={}
        def search(node,cur):
            if not node and cur:
                return False
            if not cur:
                return True
            if node.val==cur.val:
                cur=cur.next
            elif node.val==head.val:
                cur=head.next
            else:
                cur=head
            if (node.right,cur) not in memo:
                memo[(node.right,cur)]=search(node.right,cur) or search(node.right,head)
            if (node.left,cur) not in memo:
                memo[(node.left,cur)]= search(node.left,cur) or search(node.left,head)
            return memo[(node.left,cur)] or memo[(node.right,cur)]
        return search(root,head)    