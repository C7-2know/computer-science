class Solution:
    def longestPalindrome(self, s: str) -> int:
        # odd=False
        dc={}
        count=0
        # for i in s:
        #     dc[i]=dc.get(i,0)+1
        # for j in dc:
        #     if dc[j]%2==0:
        #         count+=dc[j]
        #     else:
        #         odd=True
        #         count+=(dc[j]-1)
        for i in s:
            if i in dc:
                count+=2
                dc.pop(i)
            else:
                dc[i]=1
        if len(dc)>0:
            count+=1
        # if odd:
        #     count+=1
        return count
