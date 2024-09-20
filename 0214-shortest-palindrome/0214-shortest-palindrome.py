class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)<1:
            return ""
        left,right=0,len(s)//2+1
        ls=""
        mx_p=0
        while left<right:
            ls+=s[left]
            half=s[left+1:left+1+len(ls)]
            sec_h=s[left+2:left+2+len(ls)]
            if ls==sec_h[::-1]:
                mx_p=2*(left+1)+1
            elif ls==half[::-1]:
                mx_p=2*(left+1)
            left+=1
        if mx_p==0:
            req=s[1:]
            return req[::-1]+s
        else:
            req=s[mx_p:]
            return req[::-1]+s
