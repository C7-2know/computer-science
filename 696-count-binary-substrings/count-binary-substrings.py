class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=[0,0]
        cur=s[0]
        sub=0
        for b in s:
            if cur!=b:
                count[int(b)]=0
                cur=b
            count[int(b)]+=1
            if count[int(b)]<=count[not int(b)]:
                sub+=1
        return sub