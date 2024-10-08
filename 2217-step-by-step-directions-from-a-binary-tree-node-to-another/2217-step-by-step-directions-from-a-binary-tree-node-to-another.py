# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        visited=set()
        memo={}
        start=''
        def find(node,val):
            nonlocal memo
            if not node:
                return False
            if node.val==val:
                return "u"
            left=find(node.left,val)
            if left:
                left="L"+left
            right=find(node.right,val)
            if right:
                right="R"+right
            return left if left else right
        dest=find(root,destValue)
        dest=dest[:-1]
        start=find(root,startValue)[:-1]
        i,j=0,0
        while i<len(start) and i<len(dest) and start[i]==dest[i]:
            i+=1
        start=start[i:]
        dest=dest[i:]
        print(memo)
        res='U'*len(start)+dest
        return res
            
