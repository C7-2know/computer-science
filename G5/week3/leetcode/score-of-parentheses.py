class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        dc={}
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                inner=0
                score=0
                if len(stack)>0:
                    stack.pop()
                    if len(stack)+1 in dc:
                        inner=dc[len(stack)+1]
                        dc.pop(len(stack)+1)
                    else:
                        score=1
                    dc[len(stack)]=dc.get(len(stack),0)+score+inner*2
        return dc[0]