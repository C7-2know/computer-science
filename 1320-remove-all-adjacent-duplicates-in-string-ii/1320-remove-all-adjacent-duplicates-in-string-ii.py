class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        i=0
        while i <len(s):
            if stack and stack[-1][0]==s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i],1])
            if stack[-1][1]==k:
                stack.pop()
            i+=1
        ans=""
        for v in stack:
            ans+=v[0]*v[1]
        return ans