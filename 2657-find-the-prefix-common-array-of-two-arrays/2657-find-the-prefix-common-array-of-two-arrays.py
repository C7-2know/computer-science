class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count=0
        set_a=set()
        set_b=set()
        ans=[]
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            if A[i]==B[i]:
                count+=1
                ans.append(count)
                continue
            if A[i] in set_b:
                count+=1
            if B[i] in set_a:
                count+=1
            ans.append(count)
        return ans