class Solution:
    def minimumSteps(self, s: str) -> int:
        right=1
        left=0
        swap=0
        while right<len(s):
            # print(left,s[left])
            if s[left]=='1':
                while right<len(s) and s[right]=='1':
                    right+=1
                if right<len(s):
                    s=s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]
                    swap+=1
            right+=1
            left+=1

        return swap
            
                