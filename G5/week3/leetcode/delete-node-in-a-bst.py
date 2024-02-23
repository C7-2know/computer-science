# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            curr=root
            while curr.left:
                curr=curr.left
            return curr
        def delete(root,key):
            if root==None:
                return None
            elif key< root.val:
                # print('calling from left')
                root.left=delete(root.left,key)
            elif key>root.val:
                # print('calling from right')
                root.right=delete(root.right,key)
            else:
                if not root.left and not root.right:
                    # print('first',min_)
                    return None
                elif not root.left and root.right:
                    # print('sec',min_)
                    return root.right
                elif not root.right and root.left:
                    # print('sec2',min_)
                    return root.left
                else:
                    min_=findMin(root.right)
                    # print('left min',min_.val)
                    root.val=min_.val
                    root.right=delete(root.right,min_.val)
            return root
        return delete(root,key)
                




        # def delete(node, val):
        #     if not node:
        #         return None
        #     if val > node.val:
        #         node.right = delete(node.right, val)
        #     elif val < node.val:
        #         node.left = delete(node.left, val)
        #     else:
        #         if not node.left and not node.right:
        #             return delete(node.left, val)
        #         if node.right and not node.left:
        #             return node.right
        #         if node.left and not node.right:
        #             return node.left
        #         else:
        #             # lets find the inorder succesor
        #             temp = node.right
        #             while temp.left:
        #                 temp = temp.left
        #             node.val = temp.val
        #             delete(node.right, temp.val)
                
        #     delete(root, key)
        #     return root
                    
