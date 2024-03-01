class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr=[]
        def combSum(k,n,cand,m):
            if sum(cand)==n and len(cand)==k:
                arr.append(cand[:])
            # print
            for i in range(m,10):
                cand.append(i)
                if len(cand)<=k:
                    combSum(k,n,cand,i+1)
                cand.pop()
            return
        combSum(k,n,[],1)
        return arr