class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="[":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
              
        return ceil(len(stack)/2)