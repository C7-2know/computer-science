class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        stack=[]
        n=str(n)
        i=0
        num=""
        while i<len(n):
            if stack and stack[-1][0]>n[i]:
                num=stack[-1][0]
                break
            stack.append((n[i],i))
            i+=1
        ind=0
        while stack and stack[-1][0]==num:
            num,ind=stack.pop()
        if num=="":
            return int(n)
        dec=int(n[ind])-1
        return int(n[:ind]+str(dec)+"9"*len(n[ind+1:]))
        