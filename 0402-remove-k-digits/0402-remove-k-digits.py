class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=""
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack=stack[:len(stack)-1]
                k-=1
            stack+=i
        ans=stack[:len(stack)-k]
        ans=ans.lstrip("0")
        return  ans if ans!="" else "0"