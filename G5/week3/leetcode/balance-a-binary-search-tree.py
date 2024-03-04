# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if root==None:
                return []
            left=traverse(root.left)
            right=traverse(root.right)
            return left+[root.val]+right
        inorder=traverse(root)
        def balance(arr):
            if len(arr)==0:
                return None
            if len(arr)==1:
                return TreeNode(arr[0])
            mid=len(arr)//2
            left=balance(arr[:mid])
            right=balance(arr[mid+1:])
            return TreeNode(arr[mid],left,right)
        return balance(inorder)