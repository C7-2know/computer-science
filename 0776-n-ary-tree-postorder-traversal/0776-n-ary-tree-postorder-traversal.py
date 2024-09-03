"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def trav(root):
            if not root:
                return []
            ord_=[]
            for ch in root.children:
                ord_+=trav(ch)
            ord_.append(root.val)
            return ord_
        return trav(root)
        