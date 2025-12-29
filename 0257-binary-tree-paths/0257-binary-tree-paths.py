# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths =[]
        def dfs(node, path):
            if not node.right and not node.left:
                path+=f"{node.val}"
                paths.append(path)
            path+= f"{node.val}->"
            if node.right:
                dfs(node.right, path)
            if node.left:
                dfs(node.left, path)
        dfs(root,"")
        return paths