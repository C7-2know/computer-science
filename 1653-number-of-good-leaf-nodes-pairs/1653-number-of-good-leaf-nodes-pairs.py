# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf=[]
        def dfs(node,path):
            nonlocal leaf
            if not node.left and not node.right:
                leaf.append(path[:])
            if node.left:
                dfs(node.left,path+[node.left])
            if node.right:
                dfs(node.right,path+[node.right])

        def find_dis(leaf1,leaf2,d):
            i=0
            dis=0
            while i<len(leaf1) and i<len(leaf2):
                
                if leaf1[i]!=leaf2[i]:
                    dis+=1
                if dis*2>d:
                    return False
                i+=1
            j=i-1
            if i<len(leaf1):
                return (len(leaf1)-i+dis*2)<=d
            if i<len(leaf2):
                return (len(leaf2)-i+dis*2)<=d
            return dis*2<=d
                
                
            
                
        dfs(root,[root.val])
        count=0
        for i in range(len(leaf)):
            for j in range(i+1,len(leaf)):

                if find_dis(leaf[i],leaf[j],distance):
                    count+=1
        print(count)
        return count
            
