# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        queue=[]
        ind=0
        def search(root,i):
            nonlocal ans,ind,queue
            while root:
                if i>=len(ans):
                    ans.append(root.val)
                if not root.right:
                    root=root.left
                else:
                    if root.left:
                        queue.append((root.left,i+1))
                    root=root.right
                i+=1
                ind+=1
        search(root,ind)
        while queue:
            node=queue.pop()
            # print(node[0].val)
            search(node[0],node[1])
        return ans