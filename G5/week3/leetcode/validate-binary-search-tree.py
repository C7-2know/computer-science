# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def traverse(root):
            if root==None:
                return[]
            left=traverse(root.left)
            right=traverse(root.right)
            return left+[root.val]+right
        res=traverse(root)
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True