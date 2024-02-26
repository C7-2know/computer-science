# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # def subarray(root):
        #     if root==None:
        #         return []
        #     left=subarray(root.left)
        #     right=subarray(root.right)
        #     return [root.val]+left+right
        if root==None:
            return None
        if val>root.val:
            right=self.searchBST(root.right,val)
            return right
        elif val<root.val:
            left=self.searchBST(root.left,val)
            return left
        else:
            return root
