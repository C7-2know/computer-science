# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def robb(node, rob):
            if not node:
                return 0
            if (node,rob) not in memo:
                not_rob = robb(node.left,0)+robb(node.right, 0)
                robbed=0
                if not rob:
                    robbed = robb(node.left,1) + robb(node.right,1) + node.val
                memo[(node,rob)] = max(robbed, not_rob)
            return memo[(node,rob)]
        return robb(root,0)
