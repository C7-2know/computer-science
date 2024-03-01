# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dc={}
        arr=[]
        def traverse(root,level):
            if not root:
                return [] 
            left=traverse(root.left,level+1)
            right=traverse(root.right,level+1)
            if (level+1)%2==0:
                dc[level+1]=dc.get(level+1,[])+left+right
            else:
                dc[level+1]=right+left+dc.get(level+1,[])
            return [root.val]
        if root:
            dc[0]=[root.val]
        traverse(root,0)
        ln=0
        if len(dc)>0:
            ln=max(dc.keys())
        arr=[0 for _ in range(ln)]
        for i in dc:
            if len(dc[i])==0:
                continue
            arr[i]=dc[i]
        return arr