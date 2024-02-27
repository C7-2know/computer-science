# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def halfTraverse(root):
            if root==None:
                return None
            right=halfTraverse(root.left)
            left=halfTraverse(root.right)
            return TreeNode(root.val,left,right)            
        def compare(right,left):
            if right and not left:
                return False
            elif not right and left:
                return False
            elif not right and not left:
                return True
            lef=compare(right.left,left.left)
            righ=compare(right.right,left.right)
            return lef and righ and right.val==left.val
        right=halfTraverse(root.left)
        return compare(root.right,right)