# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr=head
        mat=[[-1 for _ in range(n)] for _ in range(m)]
        s_r,s_c=0,0
        e_r=m-1
        e_c=n-1
        while curr!=None:
            for i in range(s_c,e_c+1):
                if curr==None:
                    return mat
                mat[s_r][i]=curr.val
                curr=curr.next
            for j in range(s_r+1,e_r+1):
                if curr==None:
                    return mat
                mat[j][e_c]=curr.val
                curr=curr.next
            for k in range(e_c-1,s_c,-1):
                if curr==None:
                    return mat
                mat[e_r][k]=curr.val
                curr=curr.next
            for p in range(e_r,s_r,-1):
                if curr==None:
                    return mat
                mat[p][s_c]=curr.val
                curr=curr.next
            s_c+=1
            e_c-=1
            s_r+=1
            e_r-=1
        return mat
        
