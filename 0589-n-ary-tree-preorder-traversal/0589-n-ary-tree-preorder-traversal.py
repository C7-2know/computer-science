"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return []
            if not node.children:
                return [node.val]
            ans=[node.val]
            for child in node.children:
                ans.extend(dfs(child))
            return ans
        return dfs(root)