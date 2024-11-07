# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue=[(root,0)]
        pretot=0
        while queue:
            new=[]
            tot=0
            for node,val in queue:
                if node.left and node.right:
                    sum_=node.left.val+node.right.val
                    new.append((node.left,sum_))
                    new.append((node.right,sum_))
                    tot+=sum_
                elif node.left:
                    new.append((node.left,node.left.val))
                    tot+=node.left.val
                elif node.right:
                    new.append((node.right,node.right.val))
                    tot+=node.right.val
                node.val=pretot-val
            queue=new
            pretot=tot
        return root

                    
                    
