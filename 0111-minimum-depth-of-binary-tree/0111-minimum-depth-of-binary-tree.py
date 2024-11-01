# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=[root]
        count=0
        while queue:
            count+=1
            new=[]
            for node in queue:
                if not node.left and not node.right:
                    return count
                else:
                    if node.left:
                        new.append(node.left)
                    if node.right:
                       new.append(node.right)
            queue=new
        return count
                