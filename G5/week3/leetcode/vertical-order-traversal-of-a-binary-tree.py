# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr=[]
        def traverse(root,row,col):
            if root==None:
                return 
            left=traverse(root.left,row+1,col-1)
            right=traverse(root.right,row+1,col+1)
            arr.append([root.val,row,col])
            return 
        traverse(root,0,0)
        arr.sort(key=lambda x: x[0])
        arr.sort(key=lambda x: x[1])
        arr.sort(key=lambda x: x[2])

        new=[]
        i=0
        for i in range(len(arr)):
            if i-1>=0:
                if arr[i][2]==arr[i-1][2]:
                    new[-1].append(arr[i][0])
                else:
                    new.append([arr[i][0]])
            else:
                    new.append([arr[i][0]])
        return new

