class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i=="a":
                if stack:
                    stack.pop()
                    count+=1
            else:
                stack.append(i)
        return count 