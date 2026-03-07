# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def traverse(node):
            nonlocal arr
            if not node:
                return
            traverse(node.left)
            arr.append(node.val)
            traverse(node.right)
        traverse(root)
        head=None
        node=None
        for i in arr:
            cur=TreeNode(i)
            if not node:
                node=cur
                head=node
            else:
                node.right=cur
                node=cur
        return head