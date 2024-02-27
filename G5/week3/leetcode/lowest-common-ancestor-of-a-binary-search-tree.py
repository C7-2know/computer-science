# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root,p,q):
            if root==None:
                return None
            if root.val==q or root.val==p:
                return root
            if root.val<=q and root.val>=p:
                return root
            if root.val<p:
                c_ansc=traverse(root.right,p,q)
                return c_ansc
            elif root.val>q:
                c_ansc=traverse(root.left,p,q)
                return c_ansc
        if p.val>q.val:
            p,q=q,p
        return traverse(root,p.val,q.val)

