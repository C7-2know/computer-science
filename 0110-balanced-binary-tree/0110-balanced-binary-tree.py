# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=True
        def bt(root):
            nonlocal balanced
            if not root:
                return 0
            left=bt(root.left)
            right=bt(root.right)
            if abs(left-right)>1:
                balanced=False
            return left+1 if left>right else right+1
        bt(root)
        return balanced