# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def traverse(root):
            if root== None:
                return []
            left=traverse(root.left)
            right=traverse(root.right)
            return left+[root.val]+right
        arr=traverse(root)
        return arr[k-1]