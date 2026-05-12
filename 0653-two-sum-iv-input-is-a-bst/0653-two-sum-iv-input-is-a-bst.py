# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals={}

        def traverse(node):
            if not node:
                return
            if node.val not in vals:
                vals[node.val]=0
            vals[node.val]+=1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        for num, f in vals.items():
            
            if k-num in vals:
                if k-num==num and f<=1:
                    continue
                return True
        return False