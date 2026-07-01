class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and ord(stack[-1]) != ord(c) and min(ord(stack[-1]), ord(c))+32==max(ord(stack[-1]), ord(c)):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)