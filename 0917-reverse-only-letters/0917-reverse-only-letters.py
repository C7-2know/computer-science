class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        p1,p2=0,len(s)-1
        while p1<p2:
            while p1<p2 and s[p1].isalpha()==False:
                p1+=1
            while p2>p1 and s[p2].isalpha()==False:
                p2-=1
            if  p1<p2:
                s=s[:p1]+s[p2]+s[p1+1:p2]+s[p1]+s[p2+1:]
            p1+=1
            p2-=1
        return s