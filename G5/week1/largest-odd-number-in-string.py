class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd=[]
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
               odd=num[:i+1] 
               break
        if len(odd)==0:
            return ""
        else:
            return odd
                
