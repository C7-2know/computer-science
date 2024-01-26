class Solution:
    def maxScore(self, s: str) -> int:
        left=0
        right=1
        zero=0
        one=0
        for i in range(right,len(s)):
            if s[i]=='1':
                one+=1 
        max_=zero+one
        while right<len(s):
            if s[left]=='0':
                zero+=1
            elif left!=0:
                one-=1
            # print(zero,one)
            max_=max(zero+one,max_)
            left+=1
            right+=1
        return max_
            