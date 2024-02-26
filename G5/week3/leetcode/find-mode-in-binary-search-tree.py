# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dc={}
        def traverse(root):
            if root ==None:
                return
            left=traverse(root.left)
            right=traverse(root.right)
            dc[root.val]=dc.get(root.val,0)+1 
        mode=[]
        traverse(root)
        # print(dc)
        for i in dc:
            if not mode:
                mode.append(i)
            else:
                if dc[mode[-1]]<dc[i]:
                    mode.pop()
                    mode=[i]
                elif dc[mode[-1]]==dc[i]:
                    mode.append(i)
        return mode