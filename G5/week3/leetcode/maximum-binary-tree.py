# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(sub):
            # print('called')
            if len(sub)==0:
                return None
            if len(sub)==1:
                return TreeNode(sub[-1])
            max_=max(sub)
            ind=sub.index(max_)
            left=divide(sub[:ind])
            right=divide(sub[ind+1:])
            # print(TreeNode(max_,left,right))
            return TreeNode(max_,left,right)
        return divide(nums)