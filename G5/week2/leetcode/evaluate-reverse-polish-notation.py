class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        set_=set(['+','*','-','/'])
        for i in range(len(tokens)):
            if tokens[i] in set_:
                fst=stack.pop()
                sec=stack.pop()
                res=eval(str(sec)+tokens[i]+str(fst))
                stack.append(int(res))
            else:
                stack.append(tokens[i])
        return int(stack[0])
