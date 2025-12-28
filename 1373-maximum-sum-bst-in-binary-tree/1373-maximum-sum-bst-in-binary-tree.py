# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mx =0
        def is_bst(node, min_, max_):
            cur = node.val
            if node.left and node.left.val>= cur:
                return False
            if node.right and node.right.val<= cur:
                return False
            if cur > min_ or cur < max_:
                return False
            return True
                
        def traverse(node):
            nonlocal mx
        
            if not node.left and not node.right:
                mx= max(mx, node.val)
                return node.val, node.val, node.val
            
            if node.left:
                left, ml, mxl = traverse(node.left)
            else:
                left, ml, mxl = 0, node.val, node.val
            if node.right:
                right, mr, mxr = traverse(node.right)
            else:
                right, mr, mxr = 0, node.val, node.val            
            if is_bst(node, mr, mxl):
                sum_= left+right+node.val
                mx= max(mx, sum_)
                return sum_, min(node.val, mr, ml), max(mxl, node.val, mxr)
            return float('-inf'), min(mr, ml), max(mxl, mxr)
        traverse(root)
        return max(mx, 0)
        
