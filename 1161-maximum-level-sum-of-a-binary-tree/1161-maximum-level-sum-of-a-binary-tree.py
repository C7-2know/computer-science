# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_=float('-inf')
        k=-1
        bfs=[root]
        level=0
        while bfs:
            next_=[]
            level+=1
            sum_=0
            for node in bfs:
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
                sum_+=node.val
            if sum_>max_:
                max_=sum_
                k= level
            bfs=next_
        return k
            