class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_=["(","{","["]
        close={")":0,"}":1,"]":2}
        for i in s:
            if i not in close:
                stack.append(i)
            else:
                if stack and stack[-1]==open_[close[i]]:
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
