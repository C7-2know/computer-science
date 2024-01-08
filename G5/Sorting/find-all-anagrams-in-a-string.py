class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        dp={}
        for i in p:
            dp[i]=dp.get(i,0)+1
        ds={}
        for i in s[:k]:
            ds[i]=ds.get(i,0)+1
        ind=[]
        if dp==ds:
            ind.append(0)
        for i in range(k,len(s)):
            if ds[s[i-k]]==1:
                ds.pop(s[i-k])
            else:
                ds[s[i-k]]-=1
            ds[s[i]]=ds.get(s[i],0)+1
            # print(ds,dp)
            if ds==dp:
                ind.append(i-k+1)
        return ind
        # for i in range(1,len(s)-(k-1)):
        #     # remove the first element of the previous window
        #     if ds[s[i-1]]>1:
        #         ds[s[i-1]]-=1
        #     else:
        #         ds.pop(s[i-1])
        #     # add the last element of the window
        #     ds[s[i+k-1]]=ds.get(s[i+k-1],0)+1
        #     if ds==dp:
        #         ind.append(i)
        # return ind