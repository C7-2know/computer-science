"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue=[root]
        prev=None
        while queue:
            new=[]
            for i in range(len(queue)):
                node=queue[i]
                if prev:
                    prev.next=node
                    prev=node
                else:
                    prev=node
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            prev=None
            queue=new
        return root

        