# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root,max_,min_):
            if root==None:
                return  
            self.max_=max(abs(max_-root.val),self.max_)
            self.max_=max(abs(min_-root.val),self.max_)
            max_=max(max_,root.val)
            min_=min(min_,root.val)
            left=traverse(root.left,max_,min_)
            right=traverse(root.right,max_,min_)
            return
        traverse(root,root.val,root.val)
        return self.max_
            
