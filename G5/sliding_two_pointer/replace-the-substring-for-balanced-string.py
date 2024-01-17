class Solution:
    def balancedString(self, s: str) -> int:
        dc={}
        for i in s:
            if i not in dc:
                dc[i]=0
            dc[i]+=1
        size=float('inf')
        left=0
        right=0
        max_n=max(dc.values())

        if max_n==len(s)/4:
            return 0
        while right<len(s):
            dc[s[right]]-=1
            max_n=max(dc.values())
            while max_n<=len(s)/4 and left<=right:
                dc[s[left]]=dc.get(s[left],0)+1
                size=min(size,right-left+1)
                left+=1
                max_n=max(dc.values())
            right+=1
        return 0 if size==float('inf') else int(size)
        