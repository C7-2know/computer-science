class Solution:
    def minimumSteps(self, s: str) -> int:
        right=len(s)-1
        while right>=0 and s[right]=='1':
            right-=1
        left=right-1
        swap=0
        while left>=0:
            while right>=0 and s[right]=='1':
                right-=1
            while left>=0 and s[left]=='0':
                left-=1
            if left>=0:
                # print(s[left],s[right],s,left,right)
                s=s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]
                swap+=(right-left)
            right-=1
            left-=1

        return swap
            
                