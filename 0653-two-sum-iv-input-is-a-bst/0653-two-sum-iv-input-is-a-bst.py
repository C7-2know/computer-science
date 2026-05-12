# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals=set()

        def traverse(node):
            if not node:
                return
            if k-node.val in vals:
                return True
            if node.val not in vals:
                vals.add(node.val)
            return traverse(node.left) or traverse(node.right)
        if traverse(root):
            return True
        return False
