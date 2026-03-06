class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i=1
        while i<len(s) and s[i]=='1':
            i+=1
        return True if i>=len(s) or int(s[i:],2)==0 else False