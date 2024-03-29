# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # curr=root
        # ans=[]
        # while curr!=None:
        #     ans.append(curr.val)
        #     print(curr)
        #     if curr.left:
        #         curr=curr.left
        #     else:
        #         curr=curr.right
        # return ans
        if root==None:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
