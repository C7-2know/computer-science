# class Node:
#     def __init__(self,val):

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth(n,k,opp):
            if k==1:
                if opp:
                    return 1
                return 0
            if k==2:
                if opp:
                    return 0
                return 1
            if k%2==0:
                opp= not opp
            return kth(n-1,(k+1)//2,opp)
        return kth(n,k,False)
                
            