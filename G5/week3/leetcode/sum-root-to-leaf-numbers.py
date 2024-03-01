# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total=0
        def calculate(root,val):
            nonlocal total
            if not root:
                return
            if root.left==None and root.right==None:
                val+=str(root.val)
                total+=int(val)
                return
            val+=str(root.val)
            left=calculate(root.left,val)
            right=calculate(root.right,val)
            val=val[:len(val)-1]
            return
        calculate(root,'')
        return total




        # total=0
        # dc=set()
        # def calculate(root,val):
        #     nonlocal total
        #     if not root:
        #         return
        #     if root.left==None and root.right==None:
        #         val.append(str(root.val))
        #         arr = "".join(val)
        #         total+=int(arr)
        #         val.pop()
        #         return
        #     val.append(str(root.val))
        #     left=calculate(root.left,val)
        #     right=calculate(root.right,val)
        #     val.pop()
        #     return
        # calculate(root,[])
        # return total




        # def traverse(root):   
        #     if not root:
        #         return 0,0
        #     left_s,l_deg=self.sumNumbers(root.left)
        #     right_s,r_deg=self.sumNumbers(root.right)
        #     print(right_s,left_s)
        #     return left_s+root.val*10**l_deg + right_s + root.val*10**r_deg,max(l_deg,r_deg)
        # val,deg=traverse(root)
        # return val